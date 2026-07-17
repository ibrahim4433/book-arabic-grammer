#!/bin/bash

# Stop the script if any command fails
set -e 

if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "    Created new virtual environment."
else
    echo "    Virtual environment already exists."
fi

./venv/bin/pip install -r requirements.txt

echo "==> ✅ Dependencies installed! Running system.py..."
echo "---------------------------------------------------"

# Run the python script using the virtual environment's python
./venv/bin/python debuging/build-with-id.py