# quant-notes

Study notes, flashcards, and progress tracking for:
- **MITx 15.455x** — Mathematical Methods for Quantitative Finance
- **Hull** — Options, Futures, and Other Derivatives (11th ed.)
- **Wilmott** — Paul Wilmott Introduces Quantitative Finance (2nd ed.)

## Structure

```
mitx/          MITx 15.455x modules, flashcards, problem sets
hull/          Hull chapter notes and flashcards
wilmott/       Wilmott chapter notes and flashcards
notebooklm/    NotebookLM integration scripts
sessions.json  Pomodoro session log (append-only)
```

## Math notation

Notes use LaTeX syntax rendered by KaTeX in the study app:
- Inline: `$E[X] = \mu$`
- Block: `$$\frac{dS}{S} = \mu\,dt + \sigma\,dW$$`

## NotebookLM flashcard generation

```bash
cd notebooklm
python sync_sources.py --key m04      # push sources
python fetch_artifacts.py --key m04   # pull flashcards
```

## Flashcard format

All flashcards use a unified format readable by Claude and the study app:

```markdown
---
source: notebooklm   # or "manual"
module: m04
track: mitx
---

## Card 1

**Q:** Question text

**A:** Answer text

---
```
