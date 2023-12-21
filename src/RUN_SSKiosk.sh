
# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo "Python is installed."

    # Check if venv is installed
    if command -v python3 -m venv &>/dev/null; then
        echo "venv is available."
        
        # Create and Activate ennvirontment
        python3 -m venv .kiosk
        source .kiosk/bin/activate

        # Install Python dependencies
        pip3 install -r requirements.txt

        # Run the ordering_kiosk.py script
        python3 ordering_kiosk.py

        # Deactivate the virtual environment
        deactivate
    else
        echo "Error: venv is not installed. Please install virtualenv package or use a Python version that includes venv module. You can refer to the following resources for help:"
        echo "- Official virtualenv documentation"
        echo "- [Python Packaging User Guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)"
        exit 1
    fi
else
    echo "Error: Python is not installed. Please install Python before running this script."
    exit 1
fi