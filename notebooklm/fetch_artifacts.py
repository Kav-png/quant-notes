"""
Pull generated artifacts (flashcards, quizzes) from NotebookLM back into the repo.

Usage:
    python fetch_artifacts.py --key m01 --type flashcards
    python fetch_artifacts.py --key quant --type flashcards --chapter "Hull Ch 14 — Wiener Processes & Itô's Lemma" --notes notes.md
    python fetch_artifacts.py --key m01 --type quiz

Flashcards land in:  <track-dir>/<chapter-slug>-notebooklm.md  (or flashcards/<key>-notebooklm.md if no chapter)
Quizzes land in:     questions/<key>-notebooklm.md

Requires:
    pip install "notebooklm-py[browser]"
    notebooklm login   (one-time browser auth)
"""

import argparse
import asyncio
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

import yaml
from notebooklm import NotebookLMClient
from notebooklm.rpc import QuizQuantity, QuizDifficulty

REPO_ROOT = Path(__file__).parent.parent
CONFIG_FILE = Path(__file__).parent / "config.yaml"
FLASHCARDS_DIR = REPO_ROOT / "flashcards"
QUESTIONS_DIR = REPO_ROOT / "questions"

TRACK_FLASHCARD_DIRS = {
    "hull": REPO_ROOT / "hull",
    "wilmott": REPO_ROOT / "wilmott",
    "mitx": REPO_ROOT / "mitx" / "flashcards",
}


def _slugify(text: str) -> str:
    """Convert a chapter label to a filesystem-safe slug, max 60 chars."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    text = re.sub(r"-+", "-", text)
    return text[:60].rstrip("-")


def load_config() -> dict:
    with open(CONFIG_FILE) as f:
        return yaml.safe_load(f)


def find_entry(config: dict, key: str) -> dict | None:
    for group in config.get("notebooks", {}).values():
        if key in group:
            return group[key]
    return None


def build_flashcard_instructions(chapter: str | None, notes: str | None) -> str:
    """Build a structured prompt for NotebookLM flashcard generation."""

    chapter_line = (
        f"Focus exclusively on **{chapter}** from the uploaded materials."
        if chapter
        else "Cover all key concepts from the uploaded materials."
    )

    notes_section = ""
    if notes and notes.strip():
        # Truncate notes to avoid hitting any length limits (~2000 chars is safe)
        truncated = notes.strip()[:2000]
        if len(notes.strip()) > 2000:
            truncated += "\n[...notes truncated]"
        notes_section = f"""
Also incorporate the following personal study notes — prioritise cards that \
address gaps or questions flagged in the notes:

---
{truncated}
---
"""

    return f"""{chapter_line}

Card format requirements:
- Each card tests exactly one concept, formula, or definition — no compound questions
- Formulas: front = name or plain-English description, back = the formula with all \
variables defined
- Definitions: front = term, back = precise 1–3 sentence definition + one concrete example
- Derivation steps: front = "How is X derived / what is the key insight behind X?", \
back = the critical step or intuition, not a full proof
- Pitfalls: include at least 3 cards on common mistakes or hidden assumptions \
(e.g. constant vol in BSM, log-normality assumption, no-arb prerequisites)
- Difficulty mix: 60% recall and recognition, 40% application and reasoning
- Where both Hull (market practice) and Wilmott (mathematical derivation) treat \
the same concept, note the difference on the answer side
- Format ALL math using LaTeX: inline with \\(...\\), display equations with \\[...\\]. Never use $ for math.
{notes_section}
Keep answers concise — if the answer needs more than 4 lines it should be split \
into multiple cards."""


async def fetch_flashcards(
    client,
    notebook_id: str,
    key: str,
    label: str,
    instructions: str | None,
    source_id: str | None = None,
    chapter: str | None = None,
    track: str | None = None,
    args_slug: str | None = None,
    source_ids: list[str] | None = None,
    out_dir_override: str | None = None,
) -> None:
    source_ids = source_ids if source_ids else ([source_id] if source_id else None)
    scope = f"{len(source_ids)} source(s)" if source_ids else "all sources"
    print(f"  Generating flashcards for {label} ({scope})...")
    if instructions:
        print(f"  Instructions: {instructions[:120]}...")
    status = await client.artifacts.generate_flashcards(
        notebook_id,
        source_ids=source_ids,
        instructions=instructions,
        quantity=QuizQuantity.MORE,
        difficulty=QuizDifficulty.MEDIUM,
    )
    await client.artifacts.wait_for_completion(notebook_id, status.task_id)

    slug = args_slug or (_slugify(chapter) if chapter else key)
    if out_dir_override:
        out_dir = REPO_ROOT / out_dir_override
    elif track:
        out_dir = TRACK_FLASHCARD_DIRS.get(track, REPO_ROOT / track)
    else:
        out_dir = FLASHCARDS_DIR
    out_path = out_dir / f"{slug}-notebooklm.md"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Back up existing file before overwriting so manual edits are never lost
    if out_path.exists():
        backup = out_dir / f"{slug}-notebooklm-{date.today().isoformat()}.md"
        # Avoid clobbering a backup made earlier today
        suffix = 0
        while backup.exists():
            suffix += 1
            backup = out_dir / f"{slug}-notebooklm-{date.today().isoformat()}-{suffix}.md"
        out_path.rename(backup)
        print(f"  Backed up existing cards → {backup.relative_to(REPO_ROOT)}")

    await client.artifacts.download_flashcards(notebook_id, str(out_path), output_format="markdown")
    print(f"  Saved → {out_path.relative_to(REPO_ROOT)}")


async def fetch_quiz(client, notebook_id: str, key: str, label: str) -> None:
    print(f"  Generating quiz for {label}...")
    status = await client.artifacts.generate_quiz(notebook_id)
    await client.artifacts.wait_for_completion(notebook_id, status.task_id)

    out_path = QUESTIONS_DIR / f"{key}-notebooklm.md"
    QUESTIONS_DIR.mkdir(exist_ok=True)
    await client.artifacts.download_quiz(notebook_id, str(out_path), output_format="markdown")
    print(f"  Saved → {out_path.relative_to(REPO_ROOT)}")


async def main(
    key: str,
    artifact_type: str,
    chapter: str | None,
    notes_path: Path | None,
    track: str | None,
    args_slug: str | None = None,
    notebook_id_override: str | None = None,
    source_ids_override: list[str] | None = None,
    out_dir_override: str | None = None,
) -> None:
    if notebook_id_override:
        notebook_id = notebook_id_override
        label = chapter or key
        source_id = None
    else:
        config = load_config()
        entry = find_entry(config, key)

        if entry is None:
            print(f"Key '{key}' not found in config.yaml")
            sys.exit(1)

        notebook_id = entry.get("notebook_id", "").strip()
        label = entry.get("label", key)

        if not notebook_id:
            print(f"No notebook_id set for '{key}' in config.yaml")
            sys.exit(1)

        # Resolve source_id by track (hull / wilmott) for structural scoping
        source_id = None
        if track == "hull":
            source_id = entry.get("hull_source_id", "").strip() or None
        elif track == "wilmott":
            source_id = entry.get("wilmott_source_id", "").strip() or None

        if track and not source_id:
            print(f"  WARNING: No source_id configured for track '{track}' — generating from all sources.")
            print(f"  Run: python list_sources.py  then add the ID to config.yaml")

    notes_content: str | None = None
    if notes_path and notes_path.exists():
        notes_content = notes_path.read_text(encoding="utf-8")

    instructions = build_flashcard_instructions(chapter, notes_content)

    async with await NotebookLMClient.from_storage() as client:
        if artifact_type in ("flashcards", "all"):
            await fetch_flashcards(
                client, notebook_id, key, label, instructions, source_id, chapter, track, args_slug,
                source_ids=source_ids_override,
                out_dir_override=out_dir_override,
            )
        if artifact_type in ("quiz", "all"):
            await fetch_quiz(client, notebook_id, key, label)

    print("\nDone.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", required=True, help="Config key (e.g. quant, m01)")
    parser.add_argument(
        "--type",
        choices=["flashcards", "quiz", "all"],
        default="flashcards",
        help="Which artifact to fetch",
    )
    parser.add_argument(
        "--chapter",
        default=None,
        help='Chapter or module label to focus on (e.g. "Hull Ch 14 — Wiener Processes")',
    )
    parser.add_argument(
        "--notes",
        type=Path,
        default=None,
        help="Path to a .md notes file to incorporate into the prompt",
    )
    parser.add_argument(
        "--track",
        default=None,
        help="Restrict to the source PDF for this track (hull / wilmott); also selects the output directory",
    )
    parser.add_argument(
        "--slug",
        default=None,
        help="Override the output filename stem (e.g. ch13_wiener_ito → ch13_wiener_ito-notebooklm.md)",
    )
    parser.add_argument(
        "--notebook-id",
        default=None,
        dest="notebook_id",
        help="Use this notebook_id directly, bypassing config.yaml key lookup",
    )
    parser.add_argument(
        "--source-ids",
        default=None,
        dest="source_ids",
        help="Comma-separated NLM source ids to scope generation to, overrides --track resolution",
    )
    parser.add_argument(
        "--out-dir",
        default=None,
        dest="out_dir",
        help="Output directory relative to the notes repo root, overrides --track-based directory routing",
    )
    args = parser.parse_args()
    source_ids_override = (
        [s.strip() for s in args.source_ids.split(",") if s.strip()] if args.source_ids else None
    )
    asyncio.run(main(
        args.key, args.type, args.chapter, args.notes, args.track, args.slug, args.notebook_id,
        source_ids_override, args.out_dir,
    ))
