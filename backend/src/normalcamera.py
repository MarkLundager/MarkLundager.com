from flask import Blueprint, Response
from threading import Thread
import subprocess

video_routes = Blueprint('video_routes', __name__)

class VideoStream(Thread):
    def __init__(self):
        super().__init__()
        self.command = "rpicam-vid -t 0 --inline -o -"
        self.process = None
        self.frame_generator = None
        self.is_running = False

    def start_stream(self):
        self.process = subprocess.Popen(
            self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0
        )
        self.frame_generator = self.generate_frames()
        self.is_running = True
        self.start()

    def stop_stream(self):
        if self.process and self.is_running:
            self.process.kill()
            self.join()

    def generate_frames(self):
        while self.is_running:
            frame = self.process.stdout.read(1024)
            if not frame:
                break
            yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
            )

    def run(self):
        try:
            for _ in self.frame_generator:
                pass
        finally:
            self.is_running = False

video_stream = VideoStream()

@video_routes.route('/start_stream')
def start_stream():
    video_stream.start_stream()
    return 'Streaming started.'

@video_routes.route('/stop_stream')
def stop_stream():
    video_stream.stop_stream()
    return 'Streaming stopped.'

@video_routes.route('/video_feed')
def video_feed():
    return Response(video_stream.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')