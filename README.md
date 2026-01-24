# Wheel of Heaven Image Assets

Image assets and processing pipeline for the [Wheel of Heaven](https://www.wheelofheaven.io) project.

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
├── manifest.yaml     # Processing configuration
└── mise.toml         # Task runner configuration
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
- Optional grain filter for aesthetic consistency

### Configuration

Edit `manifest.yaml` to configure image processing:

```yaml
images:
  - filename: "source-image.jpg"
    quality: 85
    grain_intensity: 0.05
    formats: ["avif", "webp"]
    enabled: true
```

### Running Processing

```bash
mise run process  # Process all enabled images
```

## Image Categories

- **Astronomical** - Stellarium screenshots, equinox visualizations
- **Illustrations** - Diagrams, infographics, AI-generated art
- **Historical** - Archival images, artifacts
- **Vectors** - Logos, icons, diagrams (SVG sources)

## Usage

Processed images are deployed to:
- Main website: `static/images/`
- CDN for optimized delivery

## License

- Original artwork: CC0-1.0 (Public Domain)
- AI-generated images: Subject to generator terms
- Third-party images: See individual metadata for attribution
