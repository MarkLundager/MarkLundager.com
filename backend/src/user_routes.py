import sqlite3
import bcrypt
from flask import Flask, request, jsonify, Blueprint
import os

user_routes = Blueprint('user_routes', __name__)

# Get the absolute path to the directory containing this script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the database file
database_path = os.path.join(current_directory, '..', 'database', 'db.sqlite')

db = sqlite3.connect(database_path)

@user_routes.route('/sign_up', methods=['POST'])
def signup():
    username = request.form.get('username')
    email    = request.form.get('email')
    password = request.form.get('password')
    c = db.cursor()
    c.execute("""
            SELECT username, email
            FROM accounts
            WHERE username = ? OR email = ? 
            """,
              (username, email)
              )
    rows = c.fetchall
    if rows:
        existing_usernames = [row[0] for row in rows]
        existing_emails = [row[1] for row in rows]

        conflicting_fields = []
        if username in existing_usernames:
            conflicting_fields.append('username')
            
        if email in existing_emails:
            conflicting_fields.append('email')

        response = jsonify({
                "error": "Username or email already exists",
                "conflicting_fields": conflicting_fields
            })
        response.status_code = 400
        return response
    else:
        db.execute("BEGIN TRANSACTION")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        c.execute("""
            INSERT INTO accounts (username, email, password, authority)
            VALUES (?, ?, ?, ?)
            """,
            (username, email, hashed_password,0)
        )
        db.commit()
        response = jsonify({"message": "User registered successfully"})
        response.status_code = 201
        return response

@user_routes.route('/sign_in', methods=['POST'])
def signin():
    username_or_email = request.form.get('username_or_email')
    password = request.form.get('password')

    c = db.cursor()
    c.execute("""
            SELECT username, email, password
            FROM accounts
            WHERE username = ? OR email = ? 
            """,
              (username_or_email, username_or_email)
              )
    user_data = c.fetchone()

    if user_data:
        stored_password = user_data[2]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            response = jsonify({"message": "Login successful"})
            response.status_code = 200
            return response
        else:
            response = jsonify({"error": "Invalid password"})
            response.status_code = 401
            return response
    else:
        response = jsonify({"error": "User not found"})
        response.status_code = 404
        return response