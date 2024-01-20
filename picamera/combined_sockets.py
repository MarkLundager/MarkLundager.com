import io
import picamera
import time
from flask import Flask, render_template, Response
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

def generate_frames():
    with picamera.PiCamera() as camera:
        camera.resolution = (720, 1280)
        camera.framerate = 20
        time.sleep(2)
        while True:
            stream = io.BytesIO()
            camera.capture(stream, format='jpeg', use_video_port=True)
            yield stream.getvalue()
            stream.seek(0)
            stream.truncate()

@app.route('/')
def index():
    return render_template('index_combined_sockets.html')

@socketio.on('connect', namespace='/video_feed')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/video_feed')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('request_frame', namespace='/video_feed')
def handle_request_frame():
    for frame in generate_frames():
        socketio.emit('video_frame', {'frame': frame}, namespace='/video_feed')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000, debug=False)