# Wheel of Heaven Image Assets

Image assets and processing pipeline for the [Wheel of Heaven](https://www.wheelofheaven.world) project.

## Overview

This repository contains all image-related assets: creative source files, raw images, and processed outputs optimized for web delivery.

## Directory Structure

```
data-images/
├── sources/          # Creative source files
│   ├── dall-e/       # AI-generated images
│   └── inkscape/     # Vector drawings and SVGs
├── raw/              # Original photographs and images
├── processed/        # Optimized output (AVIF, WebP)
├── backup/           # Backup copies
├── scripts/          # Image processing scripts
│   ├── process_images.py   # Processing pipeline
│   └── deploy_to_cdn.py    # CDN deployment
├── manifest.yaml     # Processing configuration
└── mise.toml         # Task runner configuration
```

## Quick Start

```bash
# Setup (first time only)
mise run setup

# Process images
mise run process

# Deploy to CDN
mise run deploy

# Or do both in one step
mise run full-pipeline
```

## Source Assets

### DALL-E (`sources/dall-e/`)
AI-generated images created with DALL-E for illustrations and conceptual artwork.

### Inkscape (`sources/inkscape/`)
Vector source files (.svg) for diagrams, logos, and scalable graphics.

## Image Processing

Images are processed with:
- Format conversion to AVIF and WebP
- Quality optimization (default: 80)
- Thumbnail generation (400px width)
- Optional grain filter for aesthetic consistency

### Configuration

Edit `manifest.yaml` to configure image processing:

```yaml
images:
  - filename: "source-image.jpg"
    category: "wiki"          # CDN category: wiki, timeline, library, og, icons, backgrounds
    quality: 85
    grain_intensity: 0.05
    formats: ["avif", "webp"]
    enabled: true
```

### CDN Categories

Each image has a `category` field determining where it's deployed:

| Category | Description | CDN Path |
|----------|-------------|----------|
| `wiki` | Article illustrations (default) | `/images/wiki/` |
| `timeline` | Equinox screenshots, World Ages | `/images/timeline/` |
| `library` | Book covers | `/images/library/` |
| `og` | Social sharing images | `/images/og/` |
| `icons` | Logos, symbols | `/images/icons/` |
| `backgrounds` | Hero images, patterns | `/images/backgrounds/` |

### Running Processing

```bash
mise run process        # Process all enabled images
mise run dry-run        # Preview what would be processed
mise run deploy         # Deploy to assets.wheelofheaven.world
mise run deploy-dry-run # Preview what would be deployed
mise run full-pipeline  # Process and deploy
```

## CDN Deployment

Processed images are deployed to [assets.wheelofheaven.world](https://assets.wheelofheaven.world):

```html
<!-- Reference images via CDN -->
<picture>
  <source srcset="https://assets.wheelofheaven.world/images/wiki/elohim-creation.avif" type="image/avif">
  <source srcset="https://assets.wheelofheaven.world/images/wiki/elohim-creation.webp" type="image/webp">
  <img src="https://assets.wheelofheaven.world/images/wiki/elohim-creation.webp" alt="Elohim Creation">
</picture>

<!-- Thumbnail variant for lazy loading -->
<img src="https://assets.wheelofheaven.world/images/wiki/elohim-creation_thumb.webp" alt="..." loading="lazy">
```

## Image Categories

- **Astronomical** - Stellarium screenshots, equinox visualizations
- **Illustrations** - Diagrams, infographics, AI-generated art
- **Historical** - Archival images, artifacts
- **Vectors** - Logos, icons, diagrams (SVG sources)

## License

- Original artwork: CC0-1.0 (Public Domain)
- AI-generated images: Subject to generator terms
- Third-party images: See individual metadata for attribution
