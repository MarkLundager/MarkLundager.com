import bcrypt
from flask import Flask, request, jsonify, Blueprint
from auth import create_account, login

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/create_account', methods=['POST'])
def create_account_route():
    result = create_account(request.form.get('username'), request.form.get('email'), request.form.get('password'))
    return result
@user_routes.route('/login', methods=['POST'])
def login_route():
    result = login(request.form.get('username_or_email'), request.form.get('password'))
    return result
