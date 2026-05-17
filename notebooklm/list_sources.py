"""
Print all sources in the Quant notebook with their IDs and titles.
Run this once to find the source IDs for Hull and Wilmott, then paste
them into config.yaml under quant.hull_source_id / quant.wilmott_source_id.

Usage:
    python list_sources.py
"""

import asyncio
from pathlib import Path
import yaml
from notebooklm import NotebookLMClient

CONFIG_FILE = Path(__file__).parent / "config.yaml"


async def main():
    with open(CONFIG_FILE) as f:
        config = yaml.safe_load(f)

    notebook_id = config["notebooks"]["quant"]["quant"]["notebook_id"]

    async with await NotebookLMClient.from_storage() as client:
        sources = await client.sources.list(notebook_id)

    print(f"\nSources in notebook {notebook_id}:\n")
    for src in sources:
        print(f"  id:    {src.id}")
        print(f"  title: {src.title}")
        print()

    print("Paste the IDs into config.yaml:")
    print("  quant:")
    print("    quant:")
    print("      hull_source_id: \"<id for Hull PDF>\"")
    print("      wilmott_source_id: \"<id for Wilmott PDF>\"")


if __name__ == "__main__":
    asyncio.run(main())
