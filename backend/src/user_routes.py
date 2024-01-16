import sqlite3
import bcrypt
from flask import Flask, request, jsonify, Blueprint
import os
from auth import create_account, login

user_routes = Blueprint('user_routes', __name__)
current_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(current_directory, '..', 'database', 'db.sqlite')
db = sqlite3.connect(database_path)


@user_routes.route('/create_account', methods=['POST'])
def create_account_route():
    result = create_account(db, request.form.get('username'), request.form.get('email'), request.form.get('password'))
    return result
@user_routes.route('/login', methods=['POST'])
def login_route():
    result = login(db, request.form.get('username_or_email'), request.form.get('password'))
    return result
