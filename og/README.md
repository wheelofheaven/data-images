# Open Graph image pipeline

Renders 1200x630 social-card JPEGs for every published page on
`www.wheelofheaven.world`, across all 10 site languages. Each card uses the
Bifrost design system — palette, typography, glassmorphic chip, claim-type
badge — and reads its content from the site's TOML frontmatter.

This is a sub-pipeline of `data-images/`. It uses its own venv (Playwright
dependency) and renders into a dedicated `processed/og/` subtree.

## Quick start

```bash
# One-time setup: venv + Playwright Chromium download
mise run setup

# Render everything (incremental — hash-skips unchanged entries)
python scripts/generate_og.py

# Push the rendered images to the CDN repo
python scripts/sync_og_to_cdn.py --yes

# Commit + push the assets repo to trigger Cloudflare Pages
cd ../../assets.wheelofheaven.world
git add images/og && git commit -m "Sync OG images" && git push
```

Within ~30 seconds Cloudflare rebuilds and the images go live at
`https://assets.wheelofheaven.world/images/og/{lang}/{section}/{slug}.jpg`.

## What gets rendered

The renderer auto-discovers content by walking
`../../www.wheelofheaven.world/content/{lang}/...`. For each non-draft
markdown file it produces one OG image at:

```
processed/og/{lang}/{section}/{slug}.jpg
```

Where:
- `{lang}` is `en` (no path prefix in content/) or one of `de`, `fr`, `es`,
  `ru`, `ja`, `zh`, `zh-Hant`, `ko`, `he`. Hebrew renders right-to-left
  in Frank Ruhl Libre.
- `{section}` is the top-level dir under `content/{lang}/` (e.g. `wiki`,
  `timeline`, `library`, `articles`, `news`). Top-level pages like
  `about.md` map to `section="section"`. The homepage (`content/_index.md`)
  maps to `section="default"`.
- `{slug}` is `page.slug` from frontmatter, or `index` for `_index.md`.

Section index pages and the homepage are auto-discovered too — they don't
need manifest entries.

Output is **JPEG quality 88**, ~100-125KB per image. At full saturation
(~1500 pages × 9 langs) the tree is ~165MB.

## Hash-skip incremental rendering

Each rendered JPEG gets a `.hash` sidecar containing a SHA256 of the fields
that affect output (title, summary, section_label, claim_type, lang, etc.).
On re-run, entries whose hash matches the sidecar are skipped. A full
re-render of 1500 pages takes ~70 minutes; an incremental run after a few
title edits takes seconds.

Use `--force` to bypass the sidecar and re-render everything.

## Chip i18n

The section chip in the top-left is translated per language. Labels come
from `www.wheelofheaven.world/config.toml`'s `[translations]` (default English)
and `[languages.{lang}.translations]` blocks, keyed by `navbarWiki`,
`navbarTimeline`, `navbarLibrary`, `navbarArticles`, `navbarNews`,
`navbarSources`. Adding a new language to the site automatically picks up
the chip text once those keys are translated.

## EN→non-EN field cascade

Some fields don't change by language — `author`, `publication_year`,
`original_title`, `claim_type`, `zodiac_sign`, etc. If the localized
frontmatter doesn't carry them but the EN entry does, the cascade fills
them in. This avoids editors having to repeat "Raël · 1974" in every
language file.

The cascade runs **after** the manifest merge, so handcrafted values in
`manifest.yaml` (which is EN-only) cascade to all other languages too.

## Manifest overrides

`manifest.yaml` is an override layer on top of auto-walked content. Entries
keyed by `(lang, section, slug)` replace the auto-walked entry of the same
key. Use it for:

- Section-index pages where you want non-default titles/summaries (e.g.
  the news index chip reading "NEWSROOM" instead of "DISPATCH").
- Adding metadata the source frontmatter doesn't carry, like the library
  book's author/year that then cascade to all languages.
- Special pages with custom rendering (currently rare).

Manifest entries default to `lang: en` if `lang` is omitted.

## Templates

| Template | Used for | Accent | Notes |
|---|---|---|---|
| `wiki.html.j2` | `/wiki/*` entries | cyan | Category in top-right |
| `timeline.html.j2` | `/timeline/*` ages | yellow | Bifrost SVG zodiac glyph backdrop |
| `library.html.j2` | `/library/*` books | mauve | Original title in italic subtitle |
| `articles.html.j2` | `/articles/*` explainers | lavender | Date in top-right |
| `news.html.j2` | `/news/*` dispatches | pink | Event date + "filed under" stripe |
| `section.html.j2` | section index pages | mint | Centered, no claim badge |
| `default.html.j2` | homepage / fallback | blue | Elevator-pitch composition |

All inherit from `_base.html.j2`, which provides the cosmic background,
glassmorphic chip, claim pill, and wordmark. Section accents come from
`.og--{section}` CSS classes in `_base.css`.

## CDN delivery

Rendered files mirror to `assets.wheelofheaven.world/images/og/{lang}/...` via
`scripts/sync_og_to_cdn.py`. The sync script is scoped to managed paths
(`{lang}/{section}/{slug}.jpg` only) so pre-existing brand assets at the
top of `images/og/` are left untouched.

Cloudflare Pages serves from there with a 24h `must-revalidate` cache
override on `/images/og/*` (set in the assets repo's `_headers`). This
sits below the broader `/images/*` immutable rule so re-renders propagate
within a day without needing hashed filenames or a manual purge.

## Site integration

`bifrost/templates/partials/seo.html` composes the per-page OG URL once
and reuses it for `og:image`, `twitter:image`, schema image, and preload.
Order of precedence:

1. `page.extra.image` / `page.extra.header_image` — manual override
2. Generated OG on the CDN: `{cdn_url}/images/og/{lang}/{section}/{slug}.jpg`
3. `section.extra.image` (section-level override)
4. Brand fallback (`brand/wheel-of-heaven.jpg`)

Zola's `page.components` includes the language prefix for non-default
languages (`["de", "wiki", "elohim"]`), so the composer strips it before
reading the section. Top-level pages with a single component map to
`section="section"` to match the renderer's output layout.

## Operational loop

When you change a page's title or summary on the site:

```bash
cd data-images/og
python scripts/generate_og.py            # incremental: re-renders only changed pages
python scripts/sync_og_to_cdn.py --yes   # mirror to assets repo
cd ../../assets.wheelofheaven.world
git add images/og && git commit -m "Sync OG images" && git push
```

Common one-offs:

```bash
# Render a single page (across all languages)
python scripts/generate_og.py --only wiki/elohim

# Render one language only
python scripts/generate_og.py --lang en

# Force re-render even with matching hashes
python scripts/generate_og.py --force

# Preview the plan without rendering
python scripts/generate_og.py --dry-run

# Preview the sync plan
python scripts/sync_og_to_cdn.py --dry-run
```

## Design rationale

- **Per-section accent colors** mirror the claim-badge palette so the
  site's visual vocabulary travels with the OG image (cyan / mauve /
  yellow / lavender).
- **Title in Space Grotesk** because Layer 2 in the Bifrost type system is
  the framing layer — OG titles are by definition framing.
- **Bifrost stripe at the top** — the same pastel rainbow used on the
  landing page's `bifrost-bridge` motif.
- **Glassmorphic chip** matches the navbar's blurred-translucent panel,
  so the chip reads as "site chrome" rather than "decoration".
- **Cosmic background** matches the landing-page cinematic register — deep
  blue-black, sparse starlight, single warm accent in the upper-right
  vignette.
- **Claim pill in the footer** so the epistemic status is visible on
  share cards. Cyan = direct, mauve = framework, yellow = inferred,
  lavender = speculative.
- **Voice**: copy in `manifest.yaml` and across the site is in the 2026-05
  editorial register. No "knowledge base" / "lore" / "democratization".
