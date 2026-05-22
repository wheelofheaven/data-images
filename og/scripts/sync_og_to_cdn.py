#!/usr/bin/env python3
"""
Sync rendered Open Graph images to the assets.wheelofheaven.world CDN repo.

Mirrors `data-images/og/processed/og/` → `assets.wheelofheaven.world/images/og/`.
Adds new files, updates changed ones (compared by size+mtime+hash), and
prunes stale files no longer in the source tree.

After running this, the user still needs to:
    cd ../../assets.wheelofheaven.world
    git add images/og && git commit -m "Sync OG images" && git push

Cloudflare Pages then auto-builds and the new images are live at
`https://assets.wheelofheaven.world/images/og/{lang}/{section}/{slug}.jpg`.

Usage:
    python scripts/sync_og_to_cdn.py             # mirror, with prompt before delete
    python scripts/sync_og_to_cdn.py --dry-run   # show plan, don't change anything
    python scripts/sync_og_to_cdn.py --yes       # skip the delete prompt
    python scripts/sync_og_to_cdn.py --no-prune  # never delete from destination
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / "processed" / "og"
DEFAULT_DEST = REPO_ROOT.parent.parent / "assets.wheelofheaven.world" / "images" / "og"

# Active site languages — only files under these top-level dirs are mirrored.
# Anything at `images/og/<file>` (top-level) or under non-lang dirs is left
# alone, so pre-existing brand assets (banner, background) keep their place
# and legacy PNGs from earlier renders don't pollute the deploy.
LANGUAGES = {"en", "de", "fr", "es", "ru", "ja", "zh", "zh-Hant", "ko", "he"}
ALLOWED_EXTS = {".jpg"}


def quick_signature(path: Path) -> tuple[int, int]:
    """size + mtime — cheap unchanged-check before hashing."""
    st = path.stat()
    return (st.st_size, int(st.st_mtime))


def content_hash(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _is_managed(rel: Path) -> bool:
    """Only files under `{lang}/{section}/...{ext}` are sync-managed.

    Anything outside this pattern is left untouched at both source and dest
    (top-level brand assets, legacy PNGs from earlier renders, sidecar files
    we filter out separately).
    """
    parts = rel.parts
    if len(parts) < 3:
        return False
    if parts[0] not in LANGUAGES:
        return False
    if rel.suffix not in ALLOWED_EXTS:
        return False
    return True


def plan_sync(source: Path, dest: Path) -> tuple[list[Path], list[Path], list[Path]]:
    """Return (to_copy, to_update, to_delete) — paths relative to source/dest."""
    src_files: dict[Path, Path] = {}
    for p in source.rglob("*"):
        if not p.is_file() or p.name.startswith("."):
            continue
        rel = p.relative_to(source)
        if not _is_managed(rel):
            continue
        src_files[rel] = p

    dest_files: dict[Path, Path] = {}
    if dest.exists():
        for p in dest.rglob("*"):
            if not p.is_file() or p.name.startswith("."):
                continue
            rel = p.relative_to(dest)
            if not _is_managed(rel):
                continue
            dest_files[rel] = p

    to_copy: list[Path] = []
    to_update: list[Path] = []
    for rel, sp in src_files.items():
        dp = dest_files.get(rel)
        if dp is None:
            to_copy.append(rel)
            continue
        # Cheap check first
        if quick_signature(sp) == quick_signature(dp):
            continue
        # Confirm with content hash before flagging update
        if content_hash(sp) != content_hash(dp):
            to_update.append(rel)

    to_delete: list[Path] = sorted(dest_files.keys() - src_files.keys())
    return sorted(to_copy), sorted(to_update), to_delete


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", type=Path, default=SOURCE_DIR,
                        help=f"Source tree of rendered OG images (default: {SOURCE_DIR})")
    parser.add_argument("--dest", type=Path, default=DEFAULT_DEST,
                        help=f"Destination in assets repo (default: {DEFAULT_DEST})")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the plan; make no changes.")
    parser.add_argument("--yes", action="store_true",
                        help="Don't prompt before deleting stale files.")
    parser.add_argument("--no-prune", action="store_true",
                        help="Never delete files from destination.")
    parser.add_argument("--include-sidecars", action="store_true",
                        help="Also sync .hash sidecars (default: JPEGs only).")
    args = parser.parse_args()

    if not args.source.exists():
        sys.exit(f"Source tree not found: {args.source}")
    if not args.dest.parent.exists():
        sys.exit(f"Destination parent missing: {args.dest.parent} (clone assets.wheelofheaven.world?)")
    args.dest.mkdir(parents=True, exist_ok=True)

    if args.include_sidecars:
        ALLOWED_EXTS.add(".hash")

    to_copy, to_update, to_delete = plan_sync(args.source, args.dest)

    print(f"Source: {args.source}")
    print(f"Dest:   {args.dest}")
    print(f"  copy   : {len(to_copy)} new files")
    print(f"  update : {len(to_update)} changed files")
    print(f"  delete : {len(to_delete)} stale files")

    if args.no_prune:
        to_delete = []

    if not (to_copy or to_update or to_delete):
        print("Nothing to do.")
        return 0

    if args.dry_run:
        for rel in to_copy[:20]:
            print(f"  + {rel}")
        if len(to_copy) > 20:
            print(f"  ... and {len(to_copy) - 20} more new files")
        for rel in to_update[:20]:
            print(f"  ~ {rel}")
        if len(to_update) > 20:
            print(f"  ... and {len(to_update) - 20} more changed files")
        for rel in to_delete[:20]:
            print(f"  - {rel}")
        if len(to_delete) > 20:
            print(f"  ... and {len(to_delete) - 20} more stale files")
        return 0

    if to_delete and not args.yes:
        print()
        print("Files queued for deletion:")
        for rel in to_delete[:20]:
            print(f"  - {rel}")
        if len(to_delete) > 20:
            print(f"  ... and {len(to_delete) - 20} more")
        resp = input(f"\nDelete {len(to_delete)} stale file(s) from destination? [y/N] ").strip().lower()
        if resp not in ("y", "yes"):
            print("Skipping deletion. Pass --no-prune to silence this prompt.")
            to_delete = []

    # Apply
    for rel in to_copy + to_update:
        sp = args.source / rel
        dp = args.dest / rel
        dp.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(sp, dp)
    for rel in to_delete:
        dp = args.dest / rel
        try:
            dp.unlink()
        except FileNotFoundError:
            pass

    # Clean up any now-empty section/lang dirs
    for d in sorted(args.dest.rglob("*"), key=lambda p: -len(p.parts)):
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()

    print(f"\nSynced {len(to_copy) + len(to_update)} file(s), removed {len(to_delete)}.")
    print()
    print("Next steps:")
    print(f"  cd {args.dest.parent.parent}")
    print(f"  git add images/og && git commit -m 'Sync OG images' && git push")
    print("Cloudflare Pages will auto-build and the new images go live in ~30s.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
