from flask import Flask
from flask import request, render_template
import serial
import os
import platform
import serial.tools.list_ports

app = Flask(__name__)

def setup_communication_with_arduino():
    if platform.system() == 'Linux':
        dev_path = '/dev/'
        acm_devices = [device for device in os.listdir(dev_path) if device.startswith('ttyACM')]
        
        if acm_devices:
            acm_devices.sort()  # Sort to ensure the first device is the lowest ACM number
            first_acm_device = acm_devices[0]
            return os.path.join(dev_path, first_acm_device)
        else:
            return None
    else:
        arduino_ports = [
            p.device
            for p in serial.tools.list_ports.comports()
            if 'Arduino' in p.description
        ]

        if arduino_ports:
            return arduino_ports[0]
        else:
            return None

ser = serial.Serial(setup_communication_with_arduino(), 9600, timeout=1)

@app.route('/')
def index():
    return render_template('index.html')

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
