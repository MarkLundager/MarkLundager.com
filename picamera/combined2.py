from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from picamera import PiCamera
import io
import base64
from threading import Thread
import time

app = Flask(__name__)
socketio = SocketIO(app)

class Camera:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Camera, cls).__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.frame = None
        self.thread = Thread(target=self._capture_frames)
        self.thread.daemon = True
        self.thread.start()

    def _capture_frames(self):
        with PiCamera() as camera:
            camera.resolution = (320, 240)
            camera.framerate = 15
            time.sleep(2)
            while True:
                stream = io.BytesIO()
                camera.capture(stream, format='jpeg', use_video_port=True)
                self.frame = stream.getvalue()
                stream.seek(0)
                stream.truncate()

    def get_frame(self):
        return self.frame

@app.route('/')
def index():
    return render_template('index_combined2.html')

def generate(camera):
    while True:
        frame = camera.get_frame()
        if frame is not None:
            yield frame

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('request_frame')
def handle_request_frame():
    camera = Camera()
    for frame in generate(camera):
        socketio.emit('video_frame', {'frame': base64.b64encode(frame).decode('utf-8')}, namespace='/video_feed')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)