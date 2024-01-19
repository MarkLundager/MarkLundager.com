import io
import picamera
import time
from threading import Thread

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
        with picamera.PiCamera() as camera:
            camera.resolution = (320, 240)  # Adjust the resolution as needed
            camera.framerate = 15  # Adjust the framerate as needed
            time.sleep(2)  # Allow camera to warm up
            while True:
                stream = io.BytesIO()
                camera.capture(stream, format='jpeg', use_video_port=True)
                self.frame = stream.getvalue()
                stream.seek(0)
                stream.truncate()

    def get_frame(self):
        return self.frame
