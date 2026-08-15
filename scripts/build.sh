#!/bin/bash

# Stop the script if any command fails
set -e

# Resolve repository root directory (one level up from scripts/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO_ROOT"

echo "==> 1. Syncing dependencies with uv..."
uv sync --all-extras

echo "==> 2. Building PDF with Playwright / Chrome..."
echo "---------------------------------------------------"

uv run python "$REPO_ROOT/build.py" "$@"
