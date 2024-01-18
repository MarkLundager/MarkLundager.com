import io
from flask import Blueprint, Response
import cv2
import threading

camera_routes = Blueprint('camera_routes', __name__)

class Camera:
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)  # Use the appropriate camera index

        if not self.video_capture.isOpened():
            raise Exception("Could not open video device")

        self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set the width
        self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set the height

        self.frame = None
        self.lock = threading.Lock()

        # Start a separate thread to continuously capture frames
        self.thread = threading.Thread(target=self._capture_frames, daemon=True)
        self.thread.start()

    def read(self):
        with self.lock:
            return self.frame

    def _capture_frames(self):
        while True:
            ret, frame = self.video_capture.read()
            if not ret:
                break

            with self.lock:
                self.frame = frame

    def __del__(self):
        if self.video_capture.isOpened():
            self.video_capture.release()

def generate_frames(camera):
    while True:
        frame = camera.read()
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@camera_routes.route('/video_feed')
def video_feed():
    return Response(generate_frames(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')