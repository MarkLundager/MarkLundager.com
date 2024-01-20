#!/bin/bash

# Change to the myapp directory
cd ~/MarkLundager.com

# Activate the virtual environment
source ~/venv/bin/activate

# Run the Python script
gunicorn -b localhost:8000 combined_sockets:app
#python3 backend/src/app.py

