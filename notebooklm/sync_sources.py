"""
Push local source files and URLs into the correct NotebookLM notebooks.

Usage:
    python sync_sources.py              # sync all notebooks
    python sync_sources.py --key m01    # sync one notebook by config key
    python sync_sources.py --dry-run    # show what would be uploaded

Requires:
    pip install "notebooklm-py[browser]"
    notebooklm login   (one-time browser auth)

Note: NotebookLM accepts individual YouTube video URLs. Playlist URLs may work
but if not, add individual video URLs to source_urls in config.yaml instead.
"""

import argparse
import asyncio
import sys
from pathlib import Path

import yaml
from notebooklm import NotebookLMClient

REPO_ROOT = Path(__file__).parent.parent
CONFIG_FILE = Path(__file__).parent / "config.yaml"


def load_config() -> dict:
    with open(CONFIG_FILE) as f:
        return yaml.safe_load(f)


def resolve_files(source_globs: list[str]) -> list[Path]:
    paths = []
    for pattern in source_globs:
        paths.extend(REPO_ROOT.glob(pattern))
    return sorted(set(paths))


async def sync_notebook(client, key: str, entry: dict, dry_run: bool) -> None:
    notebook_id = entry.get("notebook_id", "").strip()
    label = entry.get("label", key)
    urls = entry.get("source_urls", [])
    files = resolve_files(entry.get("source_globs", []))

    if not notebook_id:
        print(f"  [{key}] SKIP — no notebook_id set in config.yaml")
        return

    if not urls and not files:
        print(f"  [{key}] SKIP — no sources configured")
        return

    print(f"  [{key}] {label}  ({len(urls)} URLs, {len(files)} files)")

    for url in urls:
        print(f"    + URL: {url}")
        if not dry_run:
            await client.sources.add_url(notebook_id, url, wait=True)

    for src in files:
        print(f"    + {src.relative_to(REPO_ROOT)}")
        if not dry_run:
            await client.sources.add_file(notebook_id, str(src), wait=True)


async def main(target_key: str | None, dry_run: bool) -> None:
    config = load_config()
    notebooks = config.get("notebooks", {})

    # Flatten all entries into (key, entry) pairs
    entries: list[tuple[str, dict]] = []
    for group in notebooks.values():
        for key, entry in group.items():
            if target_key is None or key == target_key:
                entries.append((key, entry))

    if not entries:
        print(f"No matching notebook found for key: {target_key}")
        sys.exit(1)

    if dry_run:
        print("DRY RUN — no files will be uploaded\n")

    async with await NotebookLMClient.from_storage() as client:
        for key, entry in entries:
            await sync_notebook(client, key, entry, dry_run)

    print("\nDone.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="Config key to sync (e.g. m01, probability_statistics)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    asyncio.run(main(args.key, args.dry_run))
