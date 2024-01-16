from flask import Flask, request, render_template, jsonify, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import serial
import os
import platform
import serial.tools.list_ports
from datetime import datetime
from user_routes import user_routes
from auth import setup_user_manager,get_user

#Global variables
lamp_on = False
app = Flask(__name__, static_folder='../../frontend/build/static', template_folder='../../frontend/build')
app.config['SECRET_KEY'] = 'c190e4718d190b1e7b956ebbe9339796dc037f4a1dc4d0d5c92b9c61f84d6fe3'
login_manager = LoginManager()
setup_user_manager(app, login_manager)
app.register_blueprint(user_routes)
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
ser = serial.Serial(setup_communication_with_arduino(), 9600, timeout=1) # attempt to connect to arduino


@app.route('/')
def index():
    return render_template('index.html')
    
@login_manager.user_loader
def load_user(user_id):
    user = get_user(user_id)
    return user


@app.route('/timeUntilCanada', methods=['GET'])
def timeUntilCanada():
    return calculate_time_remaining()

@app.route('/lamp_status')
def your_endpoint():
    return jsonify({"lightOn": lamp_on})


@app.route('/run_python_code/<action>')
def run_python_code(action):
    try_attaching_to_arduino()
    if ser.is_open:
        ser.reset_input_buffer()
        if action == 'off':
            # Code for turning off
            result = execute_turn_off_code()
        elif action == 'on':
            # Code for turning on
            result = execute_turn_on_code()
    else:
        result = "Invalid action."
    data = {'message': result}
    return jsonify(data)


def execute_turn_off_code():
    global lamp_on
    while True:
        ser.write("0\n".encode('utf-8'))
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        if line == "off":
            lamp_on = False
            break
    return "Turn Off clicked! "


def execute_turn_on_code():
    global lamp_on
    while True:
        ser.write("1\n".encode('utf-8'))
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        if line == "on":
            lamp_on = True
            break
    return "Turn On clicked!"


def try_attaching_to_arduino():
    global ser
    if ser is None:
        ser = serial.Serial(setup_communication_with_arduino(), 9600, timeout=1)


def calculate_time_remaining():
    # Get the current date and time
    current_datetime = datetime.now()

    # Set the target date (June 6th)
    target_date = datetime(current_datetime.year, 6, 6)

    # Calculate the time difference
    time_difference = target_date - current_datetime
    total_seconds_remaining = int(time_difference.total_seconds())

    # Extract days, hours, minutes, and seconds
    days_remaining = time_difference.days
    hours_remaining, remainder = divmod(time_difference.seconds, 3600)
    minutes_remaining, seconds_remaining = divmod(remainder, 60)

    # Display the time remaining
    print(f"Time remaining until June 6th: {days_remaining} days, {hours_remaining} hours, {minutes_remaining} minutes, {seconds_remaining} seconds")
    return jsonify({'days': days_remaining,
                    'hours': hours_remaining,
                    'minutes': minutes_remaining,
                    'seconds': seconds_remaining,
                    'totalSeconds': total_seconds_remaining
                    })



    # Implement a function to load the user from your database
    # Example: return User(user_id, username, authority)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
