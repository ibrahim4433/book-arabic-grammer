#!/bin/bash
cd "$(dirname "$0")"

LOG_FILE=$(mktemp)
SETUP_PID=""

cleanup() {
    printf "\033[?25h" # Show cursor
    if [ -n "$SETUP_PID" ] && kill -0 $SETUP_PID 2>/dev/null; then
        kill $SETUP_PID 2>/dev/null
    fi
    rm -f "$LOG_FILE"
}

trap cleanup EXIT INT TERM

# Run setup in background
(
    set -e
    export UV_LINK_MODE=copy
    
    # Clean up temporary .venv-wsl from previous step if it exists
    if [ -d ".venv-wsl" ]; then
        rm -rf .venv-wsl
    fi
    
    VENV_DIR=".venv"
    
    # 1. Smartly detect existing venv type
    if [ -f "$VENV_DIR/Scripts/python.exe" ]; then
        echo "Detected Windows virtual environment (.venv/Scripts)."
        UV_CMD="uv.exe"
    elif [ -f "$VENV_DIR/bin/python3" ] || [ -f "$VENV_DIR/bin/python" ]; then
        echo "Detected Linux/macOS virtual environment (.venv/bin)."
        UV_CMD="uv"
    else
        # 2. No venv found, create one based on available tools
        echo "Virtual environment not found. Setting up..."
        if command -v uv &> /dev/null; then
            UV_CMD="uv"
        elif command -v uv.exe &> /dev/null; then
            UV_CMD="uv.exe"
        else
            echo "Error: Neither 'uv' nor 'uv.exe' found in PATH!"
            exit 1
        fi
        $UV_CMD venv "$VENV_DIR"
    fi
    
    if ! command -v "$UV_CMD" &> /dev/null; then
        echo "Error: Required command '$UV_CMD' is not available in PATH."
        exit 1
    fi
    
    echo "📦 Syncing dependencies via $UV_CMD..."
    export VIRTUAL_ENV="$PWD/$VENV_DIR"
    $UV_CMD pip install -e ".[dev,api]"
    
    echo "✅ Dependencies synced! Booting system..."
) > "$LOG_FILE" 2>&1 &

SETUP_PID=$!
show_logs=0
printf "\033[?25l" # Hide cursor

# Loading animation setup
frames=("⠋" "⠙" "⠹" "⠸" "⠼" "⠴" "⠦" "⠧" "⠇" "⠏")
colors=("\033[38;5;39m" "\033[38;5;38m" "\033[38;5;37m" "\033[38;5;36m" "\033[38;5;35m")
i=0
LAST_LINE=0
internal_percent=0

while kill -0 $SETUP_PID 2>/dev/null; do
    if [ $show_logs -eq 0 ]; then
        # Asymptotic progress math (caps near 99%)
        internal_percent=$(( internal_percent + (990 - internal_percent) / 10 ))
        percent=$(( internal_percent / 10 ))
        
        # Build 20-block progress bar
        bar_len=$(( percent / 5 ))
        empty_len=$(( 20 - bar_len ))
        # Generate block strings without external commands
        bar=$(printf "%0.s█" $(seq 1 $bar_len 2>/dev/null || echo ""))
        empty=$(printf "%0.s░" $(seq 1 $empty_len 2>/dev/null || echo ""))
        
        # Frame & Color
        frame=${frames[$((i % 10))]}
        color=${colors[$(( (i/2) % 5 ))]}
        
        # Render line
        printf "\r\033[K${color}%s\033[0m \033[1;36mBooting ...\033[0m \033[1;35m%3d%%\033[0m [\033[38;5;39m%s\033[38;5;239m%s\033[0m] \033[2;37m(Press 'x' for logs)\033[0m" "$frame" "$percent" "$bar" "$empty"
        
        # Wait 0.1s and read input
        read -s -n 1 -t 0.1 key || true
        if [[ $key == "x" || $key == "X" ]]; then
            show_logs=1
            printf "\r\033[K\033[1;33m--- Boot Logs ---\033[0m\n"
            cat "$LOG_FILE"
            LAST_LINE=$(wc -l < "$LOG_FILE")
        fi
        ((i++))
    else
        # If showing logs, just tail the newly added lines manually
        NEW_LINES=$(wc -l < "$LOG_FILE")
        if [ "$NEW_LINES" -gt "$LAST_LINE" ]; then
            tail -n +$((LAST_LINE + 1)) "$LOG_FILE"
            LAST_LINE=$NEW_LINES
        fi
        sleep 0.1
    fi
done

wait $SETUP_PID
EXIT_CODE=$?

printf "\033[?25h" # Show cursor
if [ $show_logs -eq 0 ]; then
    printf "\r\033[K" # Clear loading line
else
    echo -e "\n\033[1;32m✅ Boot Complete.\033[0m\n"
fi

if [ $EXIT_CODE -ne 0 ]; then
    echo -e "\n\033[1;31m❌ Boot Failed!\033[0m"
    if [ $show_logs -eq 0 ]; then
        echo -e "\n\033[1;33m--- Error Logs ---\033[0m"
        cat "$LOG_FILE"
    fi
    exit $EXIT_CODE
fi

# Remove traps and cleanup manually before exec
trap - EXIT INT TERM
rm -f "$LOG_FILE"

# Execute Python script directly
VENV_DIR=".venv"
if [ -f "$VENV_DIR/Scripts/python.exe" ]; then
    PYTHON_CMD="$VENV_DIR/Scripts/python.exe"
elif [ -f "$VENV_DIR/bin/python3" ]; then
    PYTHON_CMD="$VENV_DIR/bin/python3"
else
    PYTHON_CMD="$VENV_DIR/bin/python"
fi

exec "$PYTHON_CMD" system-workspace/tools/new-tools/system.py
