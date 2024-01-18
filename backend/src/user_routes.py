from flask import request, Blueprint, jsonify
from .auth import create_account, login, logout, is_authenticated, load_user,retrieve_lamps, User
from flask_login import LoginManager, login_required, current_user
from .arduino import send_lamp_command_to_arduino

login_manager = LoginManager()
user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/create_account', methods=['POST'])
def create_account_route():
    return create_account(request.form.get('username'), request.form.get('email'), request.form.get('password'))

@user_routes.route('/login', methods=['POST'])
def login_route():
    return login(request.form.get('username_or_email'), request.form.get('password'))


@user_routes.route('/logout', methods=['POST'])
def logout_route():
    return logout()


@user_routes.route('/is_authenticated', methods=['GET'])
def is_authenticated_route():
    return is_authenticated()

@login_manager.unauthorized_handler
def unauthorized():
    response = jsonify({"message": "User not logged in"})
    response.status_code = 403
    return response


@user_routes.route('/get_lamp_info')
@login_required 
def get_lamp_info():
    colors = retrieve_lamps(current_user.authority)
    response = jsonify({"colours": colors})
    response.status_code = 200
    return response

@user_routes.route('/send_lamp_command_to_arduino/<color>')
@login_required
def send_lamp_command_to_arduino_route(color):
    colors = retrieve_lamps(current_user.authority).split(',')
    if color in colors:
        send_lamp_command_to_arduino(color)
        response = jsonify({"message": "success"})
        response.status_code = 200
        return response
    else:
        response = jsonify({"message": "User does not have authorization for this color."})
        response.status_code = 403
        return response

@login_manager.user_loader
def user_loader(user_id):
    return load_user(user_id)