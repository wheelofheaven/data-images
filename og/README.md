# Open Graph image pipeline

Templated HTML-to-image renderer for Wheel of Heaven OG / social cards. Each
page in the site can have its own 1200x630 PNG generated from frontmatter
data, conforming to the Bifrost design system (palette, typography, claim
badges) and the 2026-05 editorial voice.

This is a sub-pipeline of `data-images/`. It uses its own venv (because of
the Playwright dependency) and renders into a dedicated `processed/og/`
subtree, but deploys to the same CDN through `data-images/scripts/deploy_to_cdn.py`
(via the `og` category).

## Status: first pass

The first-pass scope is **17 sample renders** — 12 section index pages and 5
representative content pages — to lock the design before scaling to the full
~1,251-page corpus. Once the look is signed off, the manifest gets generated
from `data-content/` and the pipeline runs across the whole site.

## Quick start

```bash
# One-time setup: venv + Playwright Chromium download
mise run setup

# Preview which entries are configured
mise run samples-dry-run

# Render the 17 samples
mise run samples
```

Output appears in `processed/og/{section}/{slug}.png`.

## How it works

1. `manifest.yaml` lists one entry per OG image. Each entry has a `section`
   (drives template choice + accent color) plus content fields like `title`,
   `summary`, `claim_type`, `category`, etc.
2. `scripts/generate_og.py` reads the manifest, renders each entry through
   the matching Jinja2 template in `templates/`, then screenshots the result
   at 1200x630 via Playwright headless Chromium.
3. Templates `@import "_base.css"` for the shared design tokens — Bifrost
   palette, the four-layer type system (Jost / Space Grotesk / IBM Plex
   Serif / iA Writer Quattro), claim-badge colors, the cosmic background.
4. Fonts are pulled from `../../www.wheelofheaven.io/static/fonts/vendor/`
   via a symlink the renderer creates at `templates/fonts/`.

## Templates

| Template | Used for | Accent | Notes |
|---|---|---|---|
| `wiki.html.j2` | `/wiki/*` entries | cyan | Category in top-right |
| `timeline.html.j2` | `/timeline/*` ages | yellow | Oversized zodiac glyph backdrop |
| `library.html.j2` | `/library/*` books | mauve | Title in Plex Serif (source register) |
| `articles.html.j2` | `/articles/*` explainers | lavender | Date in top-right |
| `news.html.j2` | `/news/*` dispatches | pink | Event date + "filed under" stripe |
| `section.html.j2` | section index pages | mint | Centered, no claim badge |
| `default.html.j2` | homepage / fallback | blue | Elevator-pitch composition |

All inherit from `_base.html.j2`, which provides the cosmic background,
section chip, claim pill, and wordmark. Section accents come from
`.og--{section}` CSS classes in `_base.css`.

## Adding entries

Edit `manifest.yaml`. The fields the renderer understands are documented in
the file header. Required: `slug`, `section`, `title`. Everything else is
optional and conditionally rendered.

For a one-off render: `python scripts/generate_og.py --only wiki/elohim`.

## Hooking into the site

The plan for the second pass:

1. Generate `manifest.yaml` from `data-content/**/*.md` frontmatter via a
   helper script (`scripts/build_manifest.py`, not yet written).
2. Render the full corpus.
3. Deploy via `../scripts/deploy_to_cdn.py` (`og` is already a valid
   category there).
4. Update `bifrost/templates/partials/seo.html` so the `og:image` fallback
   chain is: `page.extra.image` → `page.extra.og_image` →
   `https://assets.wheelofheaven.io/images/og/{section}/{slug}.png` →
   `/images/og/default.png`.

None of those steps are done yet. They land after the design is approved.

## Design rationale

- **Per-section accent colors** mirror the claim-badge palette so the site's
  visual vocabulary travels with the OG image (cyan/mauve/yellow/lavender).
- **Title in Space Grotesk** because Layer 2 in the Bifrost type system is
  the framing layer — OG titles are by definition framing.
- **Library exception**: titles render in IBM Plex Serif because the library
  is source material (Layer 3), not framing.
- **Cosmic background** matches the landing-page cinematic register — deep
  blue-black, sparse starlight, single warm accent in the upper-right vignette.
- **Claim pill in the footer** so the epistemic status is visible on share
  cards. Cyan = direct, mauve = framework, yellow = inferred, lavender =
  speculative.
- **No "knowledge base" / "lore" / "democratization" voice** anywhere. The
  copy in `manifest.yaml` is in the 2026-05 editorial register.
