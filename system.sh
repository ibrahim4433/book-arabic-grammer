#!/bin/bash
set -e

echo "==> 🚀 Starting Arabic Grammar System..."
cd "$(dirname "$0")"
export UV_LINK_MODE=copy

# Clean up temporary .venv-wsl from previous step if it exists
if [ -d ".venv-wsl" ]; then
    rm -rf .venv-wsl
fi

VENV_DIR=".venv"

# 1. Smartly detect existing venv type
if [ -f "$VENV_DIR/Scripts/python.exe" ]; then
    echo "    Detected Windows virtual environment (.venv/Scripts)."
    UV_CMD="uv.exe"
    PYTHON_CMD="$VENV_DIR/Scripts/python.exe"
elif [ -f "$VENV_DIR/bin/python3" ] || [ -f "$VENV_DIR/bin/python" ]; then
    echo "    Detected Linux/macOS virtual environment (.venv/bin)."
    UV_CMD="uv"
    if [ -f "$VENV_DIR/bin/python3" ]; then
        PYTHON_CMD="$VENV_DIR/bin/python3"
    else
        PYTHON_CMD="$VENV_DIR/bin/python"
    fi
else
    # 2. No venv found, create one based on available tools
    echo "    Virtual environment not found. Setting up..."
    # Prefer Linux uv if in native Linux/WSL, but fallback to Windows uv.exe if needed
    if command -v uv &> /dev/null; then
        UV_CMD="uv"
    elif command -v uv.exe &> /dev/null; then
        UV_CMD="uv.exe"
    else
        echo "Error: Neither 'uv' nor 'uv.exe' found in PATH!"
        exit 1
    fi
    
    $UV_CMD venv "$VENV_DIR"
    
    if [ -f "$VENV_DIR/Scripts/python.exe" ]; then
        PYTHON_CMD="$VENV_DIR/Scripts/python.exe"
    else
        PYTHON_CMD="$VENV_DIR/bin/python3"
    fi
fi

# 3. Check if the determined UV_CMD is executable
if ! command -v "$UV_CMD" &> /dev/null; then
    echo "Error: Required command '$UV_CMD' is not available in PATH."
    echo "Cannot update a Windows .venv without uv.exe, or a Linux .venv without uv."
    exit 1
fi

echo "==> 📦 Syncing dependencies via $UV_CMD..."
export VIRTUAL_ENV="$PWD/$VENV_DIR"
$UV_CMD pip install -e ".[dev,api]"

echo "==> ✅ Dependencies synced! Running system.py..."
echo "---------------------------------------------------"

# Run system.py using the exact interpreter for the venv
"$PYTHON_CMD" system-workspace/tools/new-tools/system.py
