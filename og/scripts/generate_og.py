#!/usr/bin/env python3
"""
Generate Open Graph images for Wheel of Heaven pages.

Discovers content in two ways:

1. **Auto-walk** (default): scans
   `www.wheelofheaven.io/content/{lang}/{section}/{slug}.md`, parses TOML
   frontmatter, and emits one OG per (lang, section, slug). Skips drafts.
   Covers all 9 site languages.

2. **Manifest override**: entries in `manifest.yaml` win over the same
   (lang, section, slug) key from auto-walk. Used for section indexes and
   handcrafted special pages.

Section chip labels are pulled from `www.wheelofheaven.io/config.toml`
(`navbarWiki`, `navbarLibrary`, etc.) so the chip reads in each language.

Output: `processed/og/{lang}/{section}/{slug}.jpg` — JPEG q88, with a
`.hash` sidecar so unchanged entries skip on subsequent runs.

Usage:
    python scripts/generate_og.py                       # render everything
    python scripts/generate_og.py --lang en             # one language only
    python scripts/generate_og.py --only wiki/elohim    # one slug (all langs)
    python scripts/generate_og.py --samples-only        # manifest sample: true
    python scripts/generate_og.py --no-walk             # manifest only
    python scripts/generate_og.py --force               # ignore hash sidecars
    python scripts/generate_og.py --dry-run             # print plan, no render
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import logging
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    sys.exit("PyYAML not installed. Run: pip install -r scripts/requirements.txt")

try:
    import tomllib  # Python 3.11+
except ImportError:
    try:
        import tomli as tomllib  # type: ignore
    except ImportError:
        sys.exit("tomli not installed. Run: pip install -r scripts/requirements.txt")

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError:
    sys.exit("Jinja2 not installed. Run: pip install -r scripts/requirements.txt")

try:
    from playwright.async_api import async_playwright
except ImportError:
    sys.exit(
        "Playwright not installed. Run: pip install -r scripts/requirements.txt\n"
        "Then: python -m playwright install chromium"
    )


REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = REPO_ROOT / "templates"
OUTPUT_DIR = REPO_ROOT / "processed" / "og"
SAMPLES_DIR = REPO_ROOT / "samples"
MANIFEST = REPO_ROOT / "manifest.yaml"

# www repo paths — auto-walk source + i18n source
WWW_REPO = REPO_ROOT.parent.parent / "www.wheelofheaven.io"
WWW_CONFIG = WWW_REPO / "config.toml"
WWW_CONTENT = WWW_REPO / "content"
WWW_STATIC = WWW_REPO / "static"
BRAND_DIR = WWW_STATIC / "brand"
BACKGROUND_FILE = WWW_STATIC / "images" / "essentials" / "wheel-of-heaven-background.avif"
FONT_VENDOR_DIR = WWW_STATIC / "fonts" / "vendor"

# Active site languages — `en` is the default (no path prefix in content/).
LANGUAGES = ["en", "de", "fr", "es", "ru", "ja", "zh", "zh-Hant", "ko"]

CANVAS_W = 1200
CANVAS_H = 630
JPEG_QUALITY = 88

# Section → (English fallback label, template name). The translated chip
# label is looked up per-language via LABELS; this map is the fallback and
# also picks the template per section.
SECTION_DEFAULTS = {
    "wiki": ("WIKI", "wiki"),
    "timeline": ("TIMELINE", "timeline"),
    "library": ("LIBRARY", "library"),
    "articles": ("ARTICLES", "articles"),
    "news": ("NEWSROOM", "news"),
    "sources": ("SOURCES", "section"),
    "section": ("SECTION", "section"),
    "default": ("WHEEL OF HEAVEN", "default"),
}

# Map section dirname → translation key in config.toml's [translations] blocks.
SECTION_LABEL_KEYS = {
    "wiki": "navbarWiki",
    "timeline": "navbarTimeline",
    "library": "navbarLibrary",
    "articles": "navbarArticles",
    "news": "navbarNews",
    "sources": "navbarSources",
}

# Filled by load_labels() — LABELS[lang][section] → chip text.
LABELS: dict[str, dict[str, str]] = {}


@dataclass
class Entry:
    """One OG image to render."""
    slug: str
    section: str
    title: str
    summary: str = ""
    template: str = ""
    section_label: str = ""
    claim_type: str = ""
    category: str = ""
    author: str = ""
    publication_year: str = ""
    original_title: str = ""
    date: str = ""
    event_date: str = ""
    filed_under: str = ""
    symbol: str = ""
    zodiac_sign: str = ""
    date_range: str = ""
    lang: str = "en"
    sample: bool = False
    overrides: dict[str, Any] = field(default_factory=dict)

    @property
    def key(self) -> tuple[str, str, str]:
        return (self.lang, self.section, self.slug)

    @property
    def output_path(self) -> Path:
        return OUTPUT_DIR / self.lang / self.section / f"{self.slug}.jpg"

    @property
    def title_length(self) -> str:
        n = len(self.title)
        if n > 60:
            return "xlong"
        if n > 36:
            return "long"
        return "normal"


# ---------------------------------------------------------------------------
# i18n loader
# ---------------------------------------------------------------------------

def load_labels() -> dict[str, dict[str, str]]:
    """Parse config.toml and build LABELS[lang][section] = chip text."""
    if not WWW_CONFIG.exists():
        logging.warning("www config not found at %s — using English fallbacks", WWW_CONFIG)
        return {lang: {} for lang in LANGUAGES}
    with open(WWW_CONFIG, "rb") as f:
        cfg = tomllib.load(f)
    out: dict[str, dict[str, str]] = {}
    en_t = cfg.get("translations", {})
    out["en"] = {}
    for sec, key in SECTION_LABEL_KEYS.items():
        out["en"][sec] = en_t.get(key) or SECTION_DEFAULTS[sec][0]
    for lang in LANGUAGES:
        if lang == "en":
            continue
        lang_t = cfg.get("languages", {}).get(lang, {}).get("translations", {})
        out[lang] = {}
        for sec, key in SECTION_LABEL_KEYS.items():
            out[lang][sec] = lang_t.get(key) or en_t.get(key) or SECTION_DEFAULTS[sec][0]
    return out


# ---------------------------------------------------------------------------
# Manifest loader (override layer)
# ---------------------------------------------------------------------------

def load_manifest(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path) as f:
        return yaml.safe_load(f) or {}


def normalize_manifest_entry(raw: dict) -> Entry:
    section = raw.get("section", "default")
    label_default, template_default = SECTION_DEFAULTS.get(section, SECTION_DEFAULTS["default"])
    lang = raw.get("lang", "en")
    # If section_label wasn't explicitly set in manifest, prefer the i18n label.
    section_label = raw.get("section_label")
    if not section_label:
        section_label = LABELS.get(lang, {}).get(section) or label_default
    return Entry(
        slug=raw["slug"],
        section=section,
        title=raw.get("title", ""),
        summary=raw.get("summary", "") or raw.get("description", ""),
        template=raw.get("template") or template_default,
        section_label=section_label,
        claim_type=raw.get("claim_type", ""),
        category=raw.get("category", ""),
        author=raw.get("author", ""),
        publication_year=str(raw.get("publication_year", "")),
        original_title=raw.get("original_title", ""),
        date=str(raw.get("date", "")),
        event_date=str(raw.get("event_date", "")),
        filed_under=raw.get("filed_under", ""),
        symbol=raw.get("symbol", ""),
        zodiac_sign=raw.get("zodiac_sign", ""),
        date_range=raw.get("date_range", ""),
        lang=lang,
        sample=bool(raw.get("sample", False)),
    )


# ---------------------------------------------------------------------------
# Auto-walker — discover entries from www.wheelofheaven.io/content/
# ---------------------------------------------------------------------------

_FRONTMATTER_RE = re.compile(r"^\+\+\+\s*\n(.*?)\n\+\+\+\s*\n", re.DOTALL)


def parse_frontmatter(path: Path) -> dict | None:
    """Extract TOML frontmatter from a Zola markdown file (between +++ delims)."""
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as e:
        logging.warning("Cannot read %s: %s", path, e)
        return None
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None
    try:
        return tomllib.loads(m.group(1))
    except tomllib.TOMLDecodeError as e:
        logging.debug("Bad frontmatter in %s: %s", path, e)
        return None


def _section_and_slug(rel_parts: tuple[str, ...], filename: str) -> tuple[str, str] | None:
    """Map a relative path under content/{lang}/ to (section, slug).

    content/wiki/elohim.md           → ("wiki", "elohim")
    content/wiki/_index.md           → ("wiki", "index")
    content/wiki/foo/_index.md       → skip (nested section)
    content/about.md                 → ("section", "about")   — top-level page
    content/_index.md                → ("default", "index")   — homepage
    """
    if len(rel_parts) == 0:
        return None
    if len(rel_parts) == 1:
        # Top-level file directly under content/{lang}/.
        if filename == "_index.md":
            return ("default", "index")
        return ("section", Path(filename).stem)
    section = rel_parts[0]
    if filename == "_index.md":
        if len(rel_parts) > 2:
            return None  # nested sub-section index — out of scope
        return (section, "index")
    if len(rel_parts) > 2:
        # nested page — skip for now (would need slugified path)
        return None
    return (section, Path(filename).stem)


def _str(val: Any) -> str:
    if val is None:
        return ""
    return str(val)


# Fields that don't change by language and should cascade from the EN entry
# when the localized frontmatter doesn't carry them. Library books carry
# author/year/original_title in EN only; we don't want to make editors
# duplicate that fact into 9 language files.
_CASCADE_FIELDS = ("author", "publication_year", "original_title", "zodiac_sign",
                   "symbol", "date_range", "category", "event_date", "filed_under",
                   "claim_type")


def walk_content() -> list[Entry]:
    """Discover every published page in every language."""
    if not WWW_CONTENT.exists():
        logging.warning("www content not found at %s — auto-walk disabled", WWW_CONTENT)
        return []

    entries: list[Entry] = []
    for path in WWW_CONTENT.rglob("*.md"):
        rel = path.relative_to(WWW_CONTENT)
        parts = rel.parts

        # Determine language: content/{lang}/... vs content/...
        if parts[0] in LANGUAGES and parts[0] != "en":
            lang = parts[0]
            sub = parts[1:]
        else:
            lang = "en"
            sub = parts

        # Reject paths that route into other-language subtrees from the EN walk.
        if lang == "en" and len(sub) > 0 and sub[0] in {l for l in LANGUAGES if l != "en"}:
            continue

        # Skip i18n, glossary, etc.
        if not sub:
            continue
        if sub[0] in {"i18n"}:
            continue

        result = _section_and_slug(sub, path.name)
        if result is None:
            continue
        section, slug = result

        fm = parse_frontmatter(path)
        if fm is None:
            continue
        if fm.get("draft"):
            continue

        extra = fm.get("extra") or {}
        title = _str(fm.get("title"))
        if not title:
            continue
        summary = _str(extra.get("summary") or fm.get("description"))

        # Chip label: per-language navbar* lookup, fallback to English default.
        section_label = LABELS.get(lang, {}).get(section)
        if not section_label:
            section_label = SECTION_DEFAULTS.get(section, SECTION_DEFAULTS["default"])[0]

        template = SECTION_DEFAULTS.get(section, SECTION_DEFAULTS["default"])[1]

        # date_range from start_year/end_year (timeline)
        date_range = _str(extra.get("date_range"))
        if not date_range and extra.get("start_year"):
            sy = _str(extra.get("start_year"))
            ey = _str(extra.get("end_year"))
            date_range = f"{sy} – {ey}" if ey else sy

        entries.append(Entry(
            slug=slug,
            section=section,
            title=title,
            summary=summary,
            template=template,
            section_label=section_label,
            claim_type=_str(extra.get("claim_type")),
            category=_str(extra.get("category")),
            author=_str(extra.get("author")),
            publication_year=_str(extra.get("publication_year")),
            original_title=_str(extra.get("original_title")),
            date=_str(fm.get("date")),
            event_date=_str(extra.get("event_date")),
            filed_under=_str(extra.get("filed_under")),
            symbol=_str(extra.get("symbol")),
            zodiac_sign=_str(extra.get("zodiac_sign")),
            date_range=date_range,
            lang=lang,
        ))
    return entries


def cascade_from_english(entries: list[Entry]) -> list[Entry]:
    """Fill empty language-invariant fields from the EN entry of the same (section, slug).

    Called after manifest merge so manifest-provided author/year/etc. on EN
    can cascade to non-EN entries.
    """
    en_index: dict[tuple[str, str], Entry] = {
        (e.section, e.slug): e for e in entries if e.lang == "en"
    }
    for e in entries:
        if e.lang == "en":
            continue
        ref = en_index.get((e.section, e.slug))
        if ref is None:
            continue
        for field_name in _CASCADE_FIELDS:
            if not getattr(e, field_name, ""):
                setattr(e, field_name, getattr(ref, field_name, ""))
    return entries


# ---------------------------------------------------------------------------
# Entry merging — manifest overrides win over auto-walked
# ---------------------------------------------------------------------------

def merge_entries(walked: list[Entry], manifest_entries: list[Entry]) -> list[Entry]:
    by_key: dict[tuple[str, str, str], Entry] = {e.key: e for e in walked}
    for e in manifest_entries:
        by_key[e.key] = e  # manifest wins
    return sorted(by_key.values(), key=lambda e: (e.lang, e.section, e.slug))


# ---------------------------------------------------------------------------
# Brand SVGs
# ---------------------------------------------------------------------------

def _read_brand_svg(name: str) -> str:
    path = BRAND_DIR / name
    if not path.exists():
        logging.warning("Brand SVG missing: %s — wordmark/logomark will be blank", path)
        return ""
    return path.read_text(encoding="utf-8")


BRAND_WORDMARK_SVG = _read_brand_svg("wordmark.svg")
BRAND_LOGOMARK_SVG = _read_brand_svg("logomark.svg")


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_template(env: Environment, entry: Entry) -> str:
    tpl = env.get_template(f"{entry.template}.html.j2")
    return tpl.render(
        slug=entry.slug,
        section=entry.section,
        section_label=entry.section_label,
        title=entry.title,
        summary=entry.summary,
        claim_type=entry.claim_type,
        category=entry.category,
        author=entry.author,
        publication_year=entry.publication_year,
        original_title=entry.original_title,
        date=entry.date,
        event_date=entry.event_date,
        filed_under=entry.filed_under,
        symbol=entry.symbol,
        zodiac_sign=entry.zodiac_sign,
        date_range=entry.date_range,
        lang=entry.lang,
        title_length=entry.title_length,
        meta_line=entry.category or entry.date or entry.event_date or entry.date_range,
        wordmark_svg=BRAND_WORDMARK_SVG,
        logomark_svg=BRAND_LOGOMARK_SVG,
    )


def entry_hash(entry: Entry) -> str:
    """SHA256 over the fields that affect rendered output."""
    fields = (
        entry.title, entry.summary, entry.section_label, entry.claim_type,
        entry.category, entry.author, entry.publication_year, entry.original_title,
        entry.date, entry.event_date, entry.filed_under, entry.symbol,
        entry.zodiac_sign, entry.date_range, entry.lang, entry.template, entry.section,
    )
    blob = "\x1f".join(str(f) for f in fields).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:16]


def hash_sidecar(out: Path) -> Path:
    return out.with_suffix(out.suffix + ".hash")


def ensure_font_symlink(work_dir: Path) -> None:
    """Make the www fonts visible to the rendered HTML at ./fonts/."""
    fonts_link = work_dir / "fonts"
    if fonts_link.exists() or fonts_link.is_symlink():
        return
    if not FONT_VENDOR_DIR.exists():
        logging.warning("Font vendor dir missing at %s — fallbacks will render", FONT_VENDOR_DIR)
        return
    fonts_link.symlink_to(FONT_VENDOR_DIR, target_is_directory=True)


def ensure_background_symlink(work_dir: Path) -> None:
    """Make the photographic Milky Way background visible at ./background.avif."""
    link = work_dir / "background.avif"
    if link.exists() or link.is_symlink():
        return
    if not BACKGROUND_FILE.exists():
        logging.warning("Background image missing at %s — bg will be flat", BACKGROUND_FILE)
        return
    link.symlink_to(BACKGROUND_FILE)


async def render_one(ctx, entry: Entry, html: str, work_dir: Path, force: bool) -> bool:
    out = entry.output_path
    sidecar = hash_sidecar(out)
    new_hash = entry_hash(entry)

    if out.exists() and sidecar.exists() and not force:
        if sidecar.read_text(encoding="utf-8").strip() == new_hash:
            logging.debug("skip (unchanged): %s", out.relative_to(REPO_ROOT))
            return False

    out.parent.mkdir(parents=True, exist_ok=True)

    digest = hashlib.md5(f"{entry.lang}/{entry.section}/{entry.slug}".encode()).hexdigest()[:8]
    tmp = work_dir / f".render-{digest}.html"
    tmp.write_text(html, encoding="utf-8")

    try:
        page = await ctx.new_page()
        await page.set_viewport_size({"width": CANVAS_W, "height": CANVAS_H})
        await page.goto(tmp.as_uri(), wait_until="networkidle")
        await page.evaluate("document.fonts && document.fonts.ready")
        await page.screenshot(
            path=str(out),
            type="jpeg",
            quality=JPEG_QUALITY,
            full_page=False,
            omit_background=False,
            clip={"x": 0, "y": 0, "width": CANVAS_W, "height": CANVAS_H},
        )
        await page.close()
        sidecar.write_text(new_hash, encoding="utf-8")
        logging.info("render: %s", out.relative_to(REPO_ROOT))
        return True
    finally:
        try:
            tmp.unlink()
        except FileNotFoundError:
            pass


async def render_all(entries: list[Entry], force: bool) -> tuple[int, int]:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    ensure_font_symlink(TEMPLATES_DIR)
    ensure_background_symlink(TEMPLATES_DIR)

    rendered = 0
    skipped = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        ctx = await browser.new_context(
            viewport={"width": CANVAS_W, "height": CANVAS_H},
            device_scale_factor=1,
        )
        for entry in entries:
            html = render_template(env, entry)
            ok = await render_one(ctx, entry, html, TEMPLATES_DIR, force)
            if ok:
                rendered += 1
            else:
                skipped += 1
        await ctx.close()
        await browser.close()
    return rendered, skipped


# ---------------------------------------------------------------------------
# Filtering and CLI
# ---------------------------------------------------------------------------

def filter_entries(entries: list[Entry], args) -> list[Entry]:
    if args.lang:
        wanted_langs = set(args.lang)
        entries = [e for e in entries if e.lang in wanted_langs]
    if args.samples_only:
        entries = [e for e in entries if e.sample]
    if args.only:
        wanted = set(args.only)
        entries = [e for e in entries if f"{e.section}/{e.slug}" in wanted or f"{e.lang}/{e.section}/{e.slug}" in wanted]
    return entries


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--only", action="append", default=[],
                        help="Render only this section/slug (or lang/section/slug). Repeatable.")
    parser.add_argument("--lang", action="append", default=[],
                        choices=LANGUAGES,
                        help="Restrict to these languages. Repeatable.")
    parser.add_argument("--samples-only", action="store_true",
                        help="Render only manifest entries marked sample: true")
    parser.add_argument("--no-walk", action="store_true",
                        help="Disable auto-walking site content; use manifest only.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true",
                        help="Re-render even when hash sidecar matches.")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(message)s",
    )

    # Load translations first — every entry's chip label depends on this.
    global LABELS
    LABELS = load_labels()

    manifest = load_manifest(args.manifest)
    manifest_entries = [
        normalize_manifest_entry(e) for e in manifest.get("entries", [])
        if e.get("enabled", True)
    ]

    walked = [] if args.no_walk else walk_content()
    entries = merge_entries(walked, manifest_entries)
    entries = cascade_from_english(entries)
    entries = filter_entries(entries, args)

    if args.dry_run:
        by_lang: dict[str, int] = {}
        for e in entries:
            by_lang[e.lang] = by_lang.get(e.lang, 0) + 1
        print(f"Would render {len(entries)} entries:")
        for lang, n in sorted(by_lang.items()):
            print(f"  {lang}: {n}")
        if args.verbose:
            for e in entries:
                marker = " *" if e.sample else "  "
                print(f"{marker} [{e.lang:>7}] [{e.section:>8}] {e.slug:<40} → {e.output_path.relative_to(REPO_ROOT)}")
        return

    if not entries:
        sys.exit("No entries matched filters.")

    rendered, skipped = asyncio.run(render_all(entries, args.force))
    print(f"\nDone. Rendered {rendered}, skipped {skipped}.")


if __name__ == "__main__":
    main()
