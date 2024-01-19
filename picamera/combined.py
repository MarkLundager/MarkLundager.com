import io
import picamera
import time
from flask import Flask, render_template, Response

app = Flask(__name__)

def generate_frames():
    with picamera.PiCamera() as camera:
        camera.resolution = (160, 120)
        camera.framerate = 15
        time.sleep(2)
        while True:
            stream = io.BytesIO()
            camera.capture(stream, format='jpeg', use_video_port=True)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + stream.getvalue() + b'\r\n\r\n')
            stream.seek(0)
            stream.truncate()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
