"""
split_chapters.py — one-time script to split a textbook PDF into per-chapter files.

Strategy:
  1. Try the PDF's embedded bookmarks (get_toc). Most clean PDFs have these.
  2. Fall back to parsing the printed TOC pages when bookmarks are absent:
     - Scans the first 25 pages for "Chapter N" entries and page numbers.
     - Handles two formats found in real scanned textbooks:
         a) Single-line:  "Chapter 10. Properties of stock options  214"
         b) Two-line:     "Chapter 2.\n  Mechanics of futures markets  22"
     - Tolerates OCR artifacts (e.g. "Ch11pter" instead of "Chapter").
     - Finds the PDF/book-page offset by locating where printed page "1" appears.

Tracks are read from registry.yaml — any slug registered there is accepted.
Register a new textbook first with registry_create_textbook (MCP tool) or by
editing registry.yaml directly, then run this script to split its PDF.

Usage (run from quant-notes/ directory):
    uv run --with pymupdf split_chapters.py --track hull
    uv run --with pymupdf split_chapters.py --track wilmott
    uv run --with pymupdf split_chapters.py --track hull --dry-run
    uv run --with pymupdf split_chapters.py --track stochastic_calculus
    uv run --with pymupdf split_chapters.py --track hull --no-filter

Output: quant-notes/{notes_dir}/chapters/chNN_slug.pdf
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml as _yaml
except ImportError:
    _yaml = None  # type: ignore

REPO_ROOT = Path(__file__).parent
_REGISTRY_PATH = REPO_ROOT / "registry.yaml"


def _load_track_dirs() -> dict[str, Path]:
    """Return {slug: track_dir} for every textbook in registry.yaml, falling back to a
    hard-coded set when the registry file is absent or pyyaml is not installed."""
    if _yaml is not None and _REGISTRY_PATH.exists():
        with open(_REGISTRY_PATH) as f:
            data = _yaml.safe_load(f) or {}
        return {
            slug: REPO_ROOT / meta["notes_dir"]
            for slug, meta in (data.get("textbooks") or {}).items()
        }
    # Fallback for environments without pyyaml
    return {
        "hull":    REPO_ROOT / "hull",
        "wilmott": REPO_ROOT / "wilmott",
        "mitx":    REPO_ROOT / "mitx",
    }


# Resolved lazily so the script still works without pyyaml when the caller uses
# the hardcoded fallback.
def _track_dir(slug: str) -> Path | None:
    return _load_track_dirs().get(slug)

SKIP_TITLES = {
    "index", "bibliography", "references", "preface", "foreword",
    "acknowledgment", "acknowledgements", "about the", "contents",
    "cover", "dedication", "glossary", "notation",
}

# Characters used as dot-leader fill in scanned TOCs
FILL_RE = re.compile(r'[.\s•·\xb7\x01�’‘“”]{3,}')


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")[:60]


def is_chapter(title: str) -> bool:
    t = title.lower()
    return not any(skip in t for skip in SKIP_TITLES)


def clean_title(t: str) -> str:
    t = FILL_RE.sub(" ", t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t.rstrip(".,\x01 ")


def find_pdf(track_dir: Path, pdf_name: str | None) -> Path:
    pdf_dir = track_dir / "pdfs"
    if pdf_name:
        p = pdf_dir / pdf_name
        if not p.exists():
            sys.exit(f"PDF not found: {p}")
        return p
    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if not pdfs:
        sys.exit(f"No PDFs found in {pdf_dir}")
    if len(pdfs) > 1:
        names = ", ".join(p.name for p in pdfs)
        sys.exit(f"Multiple PDFs in {pdf_dir}: {names}\nUse --pdf <filename> to pick one.")
    return pdfs[0]


# ── Method 1: embedded bookmarks ──────────────────────────────────────────────

def chapters_from_bookmarks(doc) -> list[dict]:
    toc = doc.get_toc(simple=True)
    if not toc:
        return []

    # Try level 1 first; if only 1 entry (a single wrapper), fall back to level 2
    for target_level in (1, 2):
        entries = [{"title": t, "start": p - 1} for level, t, p in toc if level == target_level]
        if len(entries) > 1:
            break

    if not entries:
        return []

    for i, ch in enumerate(entries):
        ch["end"] = entries[i + 1]["start"] if i + 1 < len(entries) else len(doc)
    return entries


# ── Method 2: parse printed TOC ───────────────────────────────────────────────

def _find_page_offset(doc) -> int:
    """0-indexed PDF page number where book page 1 is printed."""
    for i in range(15, min(60, len(doc))):
        lines = [l.strip() for l in doc[i].get_text().splitlines() if l.strip()]
        for line in lines[:4] + lines[-4:]:
            if re.fullmatch(r'1', line):
                return i
    return 0


def chapters_from_toc_text(doc) -> list[dict]:
    """Parse printed TOC from the first 25 pages, handling 1- and 2-line formats."""
    raw = "\n".join(doc[i].get_text() for i in range(4, 25))

    # Normalise fill runs (dots, bullets, spaces) immediately before a page number
    normalised = FILL_RE.sub(" ", raw)
    lines = normalised.splitlines()

    # Regex: "Ch<anything>pter N" anywhere in a line (handles cases where the
    # "Chapter" word gets merged with the previous line by the PDF text extractor)
    ch_header = re.compile(r'Ch\w{1,6}\s+(\d{1,3})[.,]?\s*(.*)')

    entries: dict[int, dict] = {}

    for i, raw_line in enumerate(lines):
        line = raw_line.strip()
        m = ch_header.search(line)
        if not m:
            continue

        num        = int(m.group(1))
        inline_rest = m.group(2).strip()  # text after "Chapter N." on the same line

        if inline_rest:
            # Single-line format: "Chapter 10. Properties of stock options  214"
            m2 = re.match(r'(.+?)\s+(\d{1,4})\s*$', inline_rest)
            if m2:
                title = clean_title(m2.group(1))
                page  = int(m2.group(2))
                entries.setdefault(num, {"num": num, "title": title, "book_page": page})
        else:
            # Two-line format: chapter number alone, title+page on next non-empty line
            for j in range(i + 1, min(i + 4, len(lines))):
                next_line = lines[j].strip()
                if not next_line:
                    continue
                m3 = re.match(r'(.+?)\s+(\d{1,4})\s*$', next_line)
                if m3:
                    title = clean_title(m3.group(1))
                    page  = int(m3.group(2))
                    entries.setdefault(num, {"num": num, "title": title, "book_page": page})
                break

    entries_list = sorted(entries.values(), key=lambda x: x["num"])

    if not entries_list:
        return []

    offset = _find_page_offset(doc)
    print(f"  Page offset: book page 1 = PDF page {offset + 1}  (offset={offset})")

    chapters = []
    for i, e in enumerate(entries_list):
        start = e["book_page"] + offset - 1   # 0-indexed PDF page
        end   = (entries_list[i + 1]["book_page"] + offset - 1) if i + 1 < len(entries_list) else len(doc)
        chapters.append({"num": e["num"], "title": e["title"], "start": start, "end": end})
    return chapters


# ── Core ──────────────────────────────────────────────────────────────────────

def build_chapters(doc, chapter_filter: bool) -> list[dict]:
    chapters = chapters_from_bookmarks(doc)
    method = "embedded bookmarks"
    if not chapters:
        print("  No embedded bookmarks — parsing printed TOC...")
        chapters = chapters_from_toc_text(doc)
        method = "printed TOC"

    if not chapters:
        sys.exit(
            "Could not extract chapter list.\n"
            "The PDF may be a scanned image without selectable text."
        )

    if chapter_filter:
        chapters = [c for c in chapters if is_chapter(c["title"])]

    if not chapters:
        sys.exit("No chapters after filtering. Try --no-filter to see all TOC entries.")

    print(f"  Source: {method}  ({len(chapters)} chapters)")
    return chapters


def run(track: str, pdf_path: Path, out_dir: Path, chapter_filter: bool, dry_run: bool):
    import fitz

    doc = fitz.open(str(pdf_path))
    print(f"\nPDF   : {pdf_path.name}  ({len(doc)} pages)")

    chapters = build_chapters(doc, chapter_filter)

    print(f"Output: {out_dir}/")
    if dry_run:
        print("\n-- DRY RUN (no files written) --")
    else:
        out_dir.mkdir(parents=True, exist_ok=True)
    print()

    for i, ch in enumerate(chapters, 1):
        n        = ch.get("num", i)
        slug     = slugify(ch["title"])
        filename = f"ch{n:02d}_{slug}.pdf"
        pages    = ch["end"] - ch["start"]
        print(f"  [{n:02d}] {ch['title'][:55]:<55}  {pages:>4}p  →  {filename}")

        if not dry_run:
            new_doc = fitz.open()
            new_doc.insert_pdf(doc, from_page=ch["start"], to_page=ch["end"] - 1)
            new_doc.save(str(out_dir / filename))
            new_doc.close()

    doc.close()
    if not dry_run:
        print(f"\nDone. {len(chapters)} files written to {out_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="Split a textbook PDF into per-chapter files.\n"
                    "Tracks are read from registry.yaml; any registered slug is accepted.",
    )
    parser.add_argument("--track",     required=True, help="Registry slug (e.g. hull, wilmott, stochastic_calculus)")
    parser.add_argument("--pdf",       help="PDF filename inside {track}/pdfs/ (auto-detected if only one)")
    parser.add_argument("--no-filter", action="store_true", help="Include all TOC entries (skip/appendix etc.)")
    parser.add_argument("--dry-run",   action="store_true", help="Print manifest without writing files")
    args = parser.parse_args()

    track_dir = _track_dir(args.track)
    if track_dir is None:
        known = ", ".join(sorted(_load_track_dirs()))
        sys.exit(
            f"Unknown track '{args.track}'.\n"
            f"Registered tracks: {known}\n"
            f"Register first with: registry_create_textbook (MCP) or edit quant-notes/registry.yaml"
        )

    run(
        args.track,
        find_pdf(track_dir, args.pdf),
        track_dir / "chapters",
        chapter_filter=not args.no_filter,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
