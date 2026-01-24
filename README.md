# Wheel of Heaven Image Assets

Processed image assets for the [Wheel of Heaven](https://www.wheelofheaven.io) website.

## Overview

This repository contains optimized images used throughout the Wheel of Heaven project. Raw images are processed into modern formats (AVIF, WebP) with consistent styling.

## Directory Structure

```
data-images/
├── raw/              # Original source images
├── processed/        # Optimized output images (AVIF, WebP)
├── backup/           # Backup copies
├── scripts/          # Image processing scripts
├── manifest.yaml     # Processing configuration
└── mise.toml         # Task runner configuration
```

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
- **Illustrations** - Diagrams, infographics
- **Historical** - Archival images, artifacts

## Usage

Processed images are deployed to the main website's `static/images/` directory or served via CDN.

## License

Images are provided under various licenses. See individual image metadata for attribution requirements.
