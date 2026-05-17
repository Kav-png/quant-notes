"""
Query NotebookLM for the table of contents of Hull and Wilmott.
"""
import asyncio, yaml
from pathlib import Path
from notebooklm import NotebookLMClient

CONFIG_FILE = Path(__file__).parent / "config.yaml"

QUESTION = (
    "List every chapter in this book with its chapter number and full title. "
    "Format each line exactly as: Ch N — Title  (use an em dash). "
    "Return only the list, no preamble."
)

async def get_toc(client, notebook_id: str, source_id: str, label: str) -> str:
    for attempt in range(1, 4):
        try:
            print(f"  [{label}] attempt {attempt}...")
            result = await client.chat.ask(notebook_id, QUESTION, source_ids=[source_id])
            return result.answer
        except Exception as e:
            print(f"  [{label}] attempt {attempt} failed: {e}")
            if attempt < 3:
                await asyncio.sleep(5)
    return "FAILED"

async def main():
    with open(CONFIG_FILE) as f:
        cfg = yaml.safe_load(f)

    entry = cfg["notebooks"]["quant"]["quant"]
    notebook_id = entry["notebook_id"]
    hull_id = entry["hull_source_id"]
    wilmott_id = entry["wilmott_source_id"]

    async with await NotebookLMClient.from_storage() as client:
        hull_toc = await get_toc(client, notebook_id, hull_id, "Hull")
        print("\n=== HULL ===\n")
        print(hull_toc)

        await asyncio.sleep(3)  # brief pause between requests

        wilmott_toc = await get_toc(client, notebook_id, wilmott_id, "Wilmott")
        print("\n=== WILMOTT ===\n")
        print(wilmott_toc)

if __name__ == "__main__":
    asyncio.run(main())
