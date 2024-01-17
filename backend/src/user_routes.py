import bcrypt
from flask import request, Blueprint, jsonify
from auth import create_account, login, logout, is_authenticated, load_user
from flask_login import LoginManager, login_required, current_user
from arduino import send_lamp_command_to_arduino

user_routes = Blueprint('user_routes', __name__)
login_manager = LoginManager()

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


@user_routes.route('/send_lamp_command_to_arduino/<color>')
@login_required
def run_python_code(color):
    send_lamp_command_to_arduino(color)

@login_manager.user_loader
def user_loader(user_id):
    load_user(user_id)