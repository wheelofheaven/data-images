#!/usr/bin/env python3
"""
Deploy processed images to assets.wheelofheaven.io repository.

Reads manifest.yaml for category mappings and copies processed images
to the appropriate subdirectories in the assets CDN repository.

Usage:
    python scripts/deploy_to_cdn.py [--output PATH] [--dry-run]

Options:
    --output PATH   Path to assets repo images directory
                    Default: ../assets.wheelofheaven.io/images
    --dry-run       Show what would be copied without copying
"""

import argparse
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed. Run: pip install pyyaml")
    sys.exit(1)


# Default paths
PROCESSED_DIR = Path(__file__).parent.parent / "processed"
DEFAULT_ASSETS_PATH = Path(__file__).parent.parent.parent / "assets.wheelofheaven.io" / "images"

# Valid categories matching assets.wheelofheaven.io structure
VALID_CATEGORIES = {"wiki", "timeline", "library", "og", "icons", "backgrounds", "hero", "earth", "brand", "news"}


def load_manifest(manifest_path: Path) -> dict:
    """Load and parse manifest.yaml."""
    with open(manifest_path) as f:
        return yaml.safe_load(f)


def get_output_files(processed_dir: Path, base_name: str) -> list[Path]:
    """Get all processed variants for an image (full + thumbnail, AVIF + WebP)."""
    files = []
    for ext in [".avif", ".webp"]:
        full = processed_dir / f"{base_name}{ext}"
        thumb = processed_dir / f"{base_name}_thumb{ext}"
        if full.exists():
            files.append(full)
        if thumb.exists():
            files.append(thumb)
    return files


def deploy(manifest_path: Path, output_path: Path, dry_run: bool = False) -> tuple[int, int]:
    """
    Deploy processed images to the assets CDN repository.

    Returns:
        Tuple of (files_deployed, files_skipped)
    """
    manifest = load_manifest(manifest_path)
    deployed = 0
    skipped = 0

    images = manifest.get("images", [])
    print(f"Processing {len(images)} images from manifest...")
    print(f"Output directory: {output_path}")
    print()

    for image in images:
        if not image.get("enabled", True):
            continue

        filename = image["filename"]
        category = image.get("category", "wiki")  # Default to wiki if not specified

        # Validate category
        if category not in VALID_CATEGORIES:
            print(f"  Warning: Invalid category '{category}' for {filename}, using 'wiki'")
            category = "wiki"

        # Get base name (handle custom output_name)
        if "output_name" in image:
            base_name = image["output_name"]
        else:
            base_name = Path(filename).stem

        # Find processed files
        files = get_output_files(PROCESSED_DIR, base_name)

        if not files:
            print(f"  Warning: No processed files found for {filename}")
            skipped += 1
            continue

        # Create destination directory
        dest_dir = output_path / category
        if not dry_run:
            dest_dir.mkdir(parents=True, exist_ok=True)

        # Copy each file
        for src_file in files:
            dest_file = dest_dir / src_file.name

            if dry_run:
                print(f"  [DRY RUN] {src_file.name} → {category}/")
            else:
                shutil.copy2(src_file, dest_file)
                print(f"  {src_file.name} → {category}/")

            deployed += 1

    return deployed, skipped


def main():
    parser = argparse.ArgumentParser(
        description="Deploy processed images to assets CDN repository"
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=DEFAULT_ASSETS_PATH,
        help=f"Path to assets repo images directory (default: {DEFAULT_ASSETS_PATH})"
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Show what would be copied without actually copying"
    )
    parser.add_argument(
        "--manifest", "-m",
        type=Path,
        default=Path(__file__).parent.parent / "manifest.yaml",
        help="Path to manifest.yaml"
    )

    args = parser.parse_args()

    # Validate paths
    if not args.manifest.exists():
        print(f"Error: Manifest not found: {args.manifest}")
        sys.exit(1)

    if not PROCESSED_DIR.exists():
        print(f"Error: Processed directory not found: {PROCESSED_DIR}")
        sys.exit(1)

    if not args.dry_run and not args.output.parent.exists():
        print(f"Error: Assets repo not found: {args.output.parent}")
        print("Make sure assets.wheelofheaven.io is cloned alongside data-images")
        sys.exit(1)

    # Run deployment
    if args.dry_run:
        print("=== DRY RUN MODE ===\n")

    deployed, skipped = deploy(args.manifest, args.output, args.dry_run)

    print()
    print(f"{'Would deploy' if args.dry_run else 'Deployed'}: {deployed} files")
    if skipped:
        print(f"Skipped: {skipped} images (no processed files found)")

    if not args.dry_run:
        print()
        print("Next steps:")
        print(f"  cd {args.output.parent}")
        print("  git add images/")
        print('  git commit -m "Update images from data-images pipeline"')
        print("  git push")


if __name__ == "__main__":
    main()
