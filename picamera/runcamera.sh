#!/bin/bash

# Change to the myapp directory
cd ~/MarkLundager.com/picamera

# Activate the virtual environment
source ~/venv/bin/activate

# Run the Python script
gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 -b 0.0.0.0:8000 combined_sockets:app
