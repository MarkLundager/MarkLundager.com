from flask import jsonify, Blueprint
import subprocess
import signal
import os

video_routes = Blueprint('video_routes', __name__)

stream_pid = None
stream_on = False

def start_video_stream():
    print("STARTING VIDEO")
    global stream_pid
    command = "rpicam-vid -t 0 --codec libav --libav-format mpegts -o 'tcp://marklundager.com/video_feed:8000'"
    process = subprocess.Popen(command, shell=True, preexec_fn=os.setsid)
    stream_pid = process.pid


def stop_video_stream():
    print("STOPPING VIDEO")
    global stream_pid
    if stream_on:
        os.killpg(os.getpgid(stream_pid), signal.SIGTERM)
        stream_on = False

@video_routes.route('/start_video_stream')
def start_video_stream_route():
    if not stream_on:
        start_video_stream
        stream_on = True
        return jsonify({'status': 'Video stream started'})
    else:
        return jsonify({'status': 'Video stream is already on'})
    
@video_routes.route('/stop_video_stream')
def stop_video_stream_route():
    global stream_on
    if stream_on:
        stop_video_stream()
        return jsonify({'status': 'Video stream stopped'})
    else:
        return jsonify({'status': 'Video stream is already off'})
