#!/bin/bash

# Change to the myapp directory
cd ~/MarkLundager.com/picamera

# Activate the virtual environment
source ~/venv/bin/activate

# Run the Python script
gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 -b 0.0.0.0:8001 combined_sockets_test_react:app &
gunicorn -b localhost:8000 ..backend.src.app:app &