import sqlite3
import bcrypt
from flask import Flask, request, jsonify, Blueprint
import os

user_routes = Blueprint('user_routes', __name__)


db = sqlite3.connect("database/db.sqlite")


@user_routes.route('/sign_up/<username>/<password>/<email>')
def signup(username,password,email):
    connection = db.cursor()
    connection.execute("""
                       SELECT username
                       
                       
                       
                       
                       """)