#!/bin/bash

# Stop the script if any command fails
set -e 

echo "==> 1. Installing system tools (you might need to enter your password)..."
sudo apt update
sudo apt install -y python3-full libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz0b

echo "==> 2. Checking for virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "    Created new virtual environment."
else
    echo "    Virtual environment already exists."
fi

echo "==> 3. Installing Python requirements..."
./venv/bin/pip install -r requirements.txt

echo "==> ✅ Dependencies installed!
echo "---------------------------------------------------"
