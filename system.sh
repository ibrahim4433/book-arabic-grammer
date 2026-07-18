#!/bin/bash
set -e

echo "==> 🚀 Starting Arabic Grammar System..."

# Ensure we are running from the script's location (the root)
cd "$(dirname "$0")"

# Suppress uv cross-filesystem hardlink warnings in WSL
export UV_LINK_MODE=copy

if [ ! -d ".venv" ]; then
    echo "    Virtual environment not found. Setting up..."
    uv venv
fi

echo "==> 📦 Syncing dependencies via uv..."
uv pip install -e ".[dev,api]"

echo "==> ✅ Dependencies synced! Running system.py..."
echo "---------------------------------------------------"

# Run system.py using the modern uv virtual environment
uv run python system-workspace/tools/new-tools/system.py
