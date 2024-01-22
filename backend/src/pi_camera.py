import io
import picamera
import time
from flask import Flask, render_template
from flask_socketio import SocketIO

socketapp = Flask(__name__)
#socketio = SocketIO(socketapp)
socketio = SocketIO(socketapp, cors_allowed_origins="https://www.marklundager.com")
connected = 0
generate_frames_flag = False  # Shared flag to track if frames are being generated

def generate_frames():
    global generate_frames_flag
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


@socketapp.route('/home')
def index():
    return render_template('index_combined_sockets_test.html')

@socketio.on('connect', namespace='/video_feed')
def handle_connect():
    global connected
    global generate_frames_flag
    connected += 1
    print('Client connected')

@socketio.on('disconnect', namespace='/video_feed')
def handle_disconnect():
    global connected
    global generate_frames_flag
    connected -= 1
    if connected == 0:
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
    socketio.run(socketapp, host='0.0.0.0', port=8001, debug=True)