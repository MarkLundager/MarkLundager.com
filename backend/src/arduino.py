import serial
import os
import platform
import serial.tools.list_ports


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

def try_attaching_to_arduino():
    global ser
    if ser is None:
        ser = serial.Serial(setup_communication_with_arduino(), 9600, timeout=1)


def send_lamp_command_to_arduino(color):

    try_attaching_to_arduino()
    if ser.is_open:
        ser.reset_input_buffer()
        while True:
            command = color + "\n"
            ser.write(command.encode('utf-8'))
            line = ser.readline().decode('utf-8').rstrip()
            if line == "success" or line == "failure":
                break
        return line
    else:
        return "Could not connect to arduino"


