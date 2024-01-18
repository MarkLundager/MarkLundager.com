import picamera
import io
from flask import Blueprint, Response
import threading

camera_routes = Blueprint('camera_routes', __name__)
thread_lock = threading.Lock()
@camera_routes.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def background_thread():
    with app.app_context():
        global thread_lock
        with thread_lock:
            frames = generate_frames()
            app.frames_iterator = iter(frames)


def generate_frames():
    with picamera.PiCamera() as cam:
        cam.resolution = (640, 480)
        cam.framerate = 30

        while True:
            stream = io.BytesIO()
            cam.capture(stream, 'jpeg', use_video_port=True)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + stream.getvalue() + b'\r\n')