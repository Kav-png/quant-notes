#!/usr/bin/env bash
# One-time setup for the NotebookLM integration.
# Run from the repo root: bash notebooklm/setup.sh

set -e

echo "==> Installing notebooklm-py..."
pip install "notebooklm-py[browser]"
playwright install chromium

echo ""
echo "==> Authenticating with Google (opens a browser window)..."
notebooklm login

echo ""
echo "==> Auth complete. Next steps:"
echo "    1. Create a notebook for each module:"
echo "       notebooklm create 'M01 — Probability'"
echo "       notebooklm list   # copy the notebook ID"
echo ""
echo "    2. Paste each ID into notebooklm/config.yaml"
echo ""
echo "    3. Sync sources for a module:"
echo "       python notebooklm/sync_sources.py --key m01"
echo ""
echo "    4. Fetch generated flashcards/quizzes:"
echo "       python notebooklm/fetch_artifacts.py --key m01 --type all"
