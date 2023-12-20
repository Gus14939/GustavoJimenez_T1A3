#!/bin/bash

# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo "Python is installed."

    # Check if venv is installed
    if command -v python3 -m venv &>/dev/null; then
        echo "venv is available."
        
        # Add your additional commands here
        # For example, create and activate a virtual environment
        python3 -m venv .kiosk
        source myvenv/bin/activate

        # Install Python dependencies
        pip3 install -r requirements.txt

        # Run the ordering_kiosk.py script
        python3 ordering_kiosk.py

        # Deactivate the virtual environment
        deactivate
    else
        echo "Error: venv is not installed. Please install virtualenv package or use a Python version that includes venv module."
        exit 1
    fi
else
    echo "Error: Python is not installed. Please install Python before running this script."
    exit 1
fi

#APP_NAME="Self Serving Kiosk Terminal"

python3 -m venv .kiosk
source .kiosk/bin/activate
pip3 install -r requirements.txt

python3 ordering_kiosk.py

