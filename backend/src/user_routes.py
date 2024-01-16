import sqlite3
import bcrypt
from flask import Flask, request, jsonify, Blueprint
import os
from auth import sign_up, sign_in

user_routes = Blueprint('user_routes', __name__)
current_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(current_directory, '..', 'database', 'db.sqlite')
db = sqlite3.connect(database_path)


@user_routes.route('/sign_up', methods=['POST'])
def sign_up_route():
    result = sign_up(db, request.form.get('username'), request.form.get('email'), request.form.get('password'))
    return result
@user_routes.route('/sign_in', methods=['POST'])
def sign_in_route():
    result = sign_in(db, request.form.get('username_or_email'), request.form.get('password'))
    return result
