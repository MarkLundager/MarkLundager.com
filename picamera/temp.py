from flask import Flask, render_template

app = Flask(__name__)


generate_frames_flag = False  # Shared flag to track if frames are being generated



@app.route('/')
def index():
    return render_template('index_combined_sockets_test.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)