import io
import picamera
import time
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS
import threading

socketapp = Flask(__name__)
CORS(socketapp)
socketio = SocketIO(socketapp, cors_allowed_origins="*")
connected_clients = 0
generate_frames_flag = False
camera_lock = threading.Lock()

def generate_frames():
    global generate_frames_flag
    with picamera.PiCamera() as camera:
        camera.resolution = (300, 250)
        camera.framerate = 20
        time.sleep(2)
        while True:
            if generate_frames_flag:
                try:
                    with camera_lock:
                        stream = io.BytesIO()
                        camera.capture(stream, format='jpeg', use_video_port=True)
                        yield stream.getvalue()
                except Exception as e:
                    print(f"Error capturing frame: {e}")
                    break

@socketapp.route('/home')
def index():
    return render_template('index_combined_sockets_test.html')

@socketio.on('connect', namespace='/video_feed')
def handle_connect():
    global connected_clients
    with camera_lock:
        connected_clients += 1
        print('Client connected')

@socketio.on('disconnect', namespace='/video_feed')
def handle_disconnect():
    global connected_clients
    global generate_frames_flag
    with camera_lock:
        connected_clients -= 1
        if connected_clients == 0:
            generate_frames_flag = False
        print('Client disconnected')

@socketio.on('request_frame', namespace='/video_feed')
def handle_request_frame():
    global generate_frames_flag
    if not generate_frames_flag:
        print("going to send frames")
        generate_frames_flag = True
        for frame in generate_frames():
            print("sending frames")
            if generate_frames_flag:
                socketio.emit('video_frame', {'frame': frame}, namespace='/video_feed')
            else:
                break
    else:
        print('Frames are already being generated. Ignoring request.')

if __name__ == '__main__':
    try:
        socketio.run(socketapp, host='0.0.0.0', port=8001, debug=True)
    finally:
        # Release camera resources when the application exits
        with camera_lock:
            generate_frames_flag = False