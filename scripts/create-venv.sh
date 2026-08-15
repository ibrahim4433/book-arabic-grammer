#!/bin/bash

# Stop the script if any command fails
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO_ROOT"

echo "==> 1. Installing / Syncing virtual environment via uv..."
uv sync --all-extras

echo "==> 2. Installing Playwright Chromium browser..."
uv run playwright install chromium

echo "==> ✅ Environment and dependencies are ready!"
echo "---------------------------------------------------"
