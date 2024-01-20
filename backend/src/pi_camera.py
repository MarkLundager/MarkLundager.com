import io
import picamera
import time
from flask import Flask, render_template
from flask_socketio import SocketIO

socketio = None

generate_frames_flag = False  # Shared flag to track if frames are being generated


def generate_frames():
    with picamera.PiCamera() as camera:
        camera.resolution = (300), (250)
        camera.framerate = 20
        time.sleep(2)
        while True:
            if generate_frames_flag:
                stream = io.BytesIO()
                camera.capture(stream, format='jpeg', use_video_port=True)
                yield stream.getvalue()
                stream.seek(0)
                stream.truncate()

@socketio.on('connect', namespace='/video_feed')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/video_feed')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('request_frame', namespace='/video_feed')
def handle_request_frame():
    global generate_frames_flag
    if not generate_frames_flag:
        generate_frames_flag = True
        for frame in generate_frames():
            socketio.emit('video_frame', {'frame': frame}, namespace='/video_feed')
    else:
        print('Frames are already being generated. Ignoring request.')