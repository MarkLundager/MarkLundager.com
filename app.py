from flask import Flask
from flask import request
import serial
import os

app = Flask(__name__)

def find_first_ttyacm():
    dev_path = '/dev/'
    acm_devices = [device for device in os.listdir(dev_path) if device.startswith('ttyACM')]
    
    if acm_devices:
        acm_devices.sort()  # Sort to ensure the first device is the lowest ACM number
        first_acm_device = acm_devices[0]
        return os.path.join(dev_path, first_acm_device)
    else:
        return None

ser = serial.Serial(find_first_ttyacm(), 9600, timeout=1)

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Buttons Page</title>
    </head>
    <body>
        <h1>Welcome to marklundager.com</h1>
        <p>Click the buttons below:</p>
        <button onclick="buttonClicked('off')">Turn Off</button>
        <button onclick="buttonClicked('on')">Turn On</button>

        <script>
            function buttonClicked(action) {
                // Send a request to the Flask API endpoint with the button action
                fetch(`/run_python_code/${action}`)
                    .then(response => response.json())
                    .catch(error => {
                        console.error('Error:', error);
                    });
            }
        </script>
    </body>
    </html>
    """

@app.route('/run_python_code/<action>')
def run_python_code(action):
    if action == 'off':
        # Code for turning off
        result = execute_turn_off_code()
    elif action == 'on':
        # Code for turning on
        result = execute_turn_on_code()
    else:
        result = "Invalid action."

    return {'message': result}

def execute_turn_off_code():
    ser.reset_input_buffer()

    while True:
        ser.write("0\n".encode('utf-8'))
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        if line == "off":
            break

    return "Turn Off clicked! Run Python code to turn off."

def execute_turn_on_code():
    ser.reset_input_buffer()

    while True:
        ser.write("1\n".encode('utf-8'))
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        if line == "on":
            break

    return "Turn On clicked! Run Python code to turn on."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
