#!/bin/bash

# Change to the myapp directory
cd ~/marklundager.com

# Activate the virtual environment
source ~/venv/bin/activate


# Run the Python script
#gunicorn -k gevent -w 1 -b 0.0.0.0:8000 backend.src.app:app
#gunicorn -b localhost:8000 backend.src.app:app

python3 backend/src/pi_camera.py &
gunicorn -b localhost:8000 backend.src.app:app &
#gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 -b 0.0.0.0:8001 backend.src.pi_camera:app &
#gunicorn -b localhost:8000 backend.src.app:app &
#gunicorn -b localhost:8001 backend.src.pi_camera:app &




