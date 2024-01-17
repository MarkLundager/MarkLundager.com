import sqlite3
import bcrypt
from flask_login import UserMixin, login_user,logout_user,  current_user
from flask import jsonify
import os



class User(UserMixin):
    def __init__(self, user_id, username, authority):
        self.id = user_id
        self.username = username
        self.authority = authority

def create_account( username, email, password):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    database_path = os.path.join(current_directory, '..', 'database', 'db.sqlite')
    db = sqlite3.connect(database_path)
    c = db.cursor()
    c.execute("""
            SELECT username, email
            FROM accounts
            WHERE username = ? OR email = ? 
            """,
            (username, email)
            )
    rows = c.fetchall()
    if rows:
        existing_usernames = [row[0] for row in rows]
        existing_emails = [row[1] for row in rows]

        conflicting_fields = []
        if username in existing_usernames:
            conflicting_fields.append('username')
            
        if email in existing_emails:
            conflicting_fields.append('email')

        response = jsonify({
                "errorMessage": "Username or email already exists",
                "conflicting_fields": conflicting_fields
            })
        response.status_code = 400
        c.close()
        db.close()
        return response
    else:
        db.execute("BEGIN TRANSACTION")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        c.execute("""
            INSERT INTO accounts (username, email, password_hash, authority)
            VALUES (?, ?, ?, ?)
            """,
            (username, email, hashed_password,0)
        )
        db.commit()
        response = jsonify({"message": "User registered successfully"})
        response.status_code = 201
        c.close()
        db.close()
        return response

def login(username_or_email, password):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    database_path = os.path.join(current_directory, '..', 'database', 'db.sqlite')
    db = sqlite3.connect(database_path)
    c = db.cursor()
    c.execute("""
            SELECT id, username, email, password_hash, authority
            FROM accounts
            WHERE username = ? OR email = ? 
            """,
            (username_or_email, username_or_email)
            )
    user_data = c.fetchone()
    c.close()
    db.close()
    if user_data:
        stored_password_hash = user_data[3]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):
            response = jsonify({"message": "Login successful"})
            response.status_code = 200
            user = User(user_data[0], user_data[1], user_data[4])
            login_user(user, remember=True)
            return response
        else:
            response = jsonify({"error": "Invalid password"})
            response.status_code = 401
            return response
    else:
        response = jsonify({"error": "User not found"})
        response.status_code = 404
        return response


def load_user(user_id):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    database_path = os.path.join(current_directory, '..', 'database', 'db.sqlite')
    db = sqlite3.connect(database_path)
    c = db.cursor()
    c.execute("""
            SELECT id, username, authority
            FROM accounts
            WHERE id = ? 
            """,
            (str(user_id))
            )
    user_data = c.fetchone()
    c.close()
    db.close()
    if user_data:
        user = User(user_data[0], user_data[1],user_data[2])
        return user
    else:
        return None

def is_authenticated():
    response = jsonify({
        "is_authenticated": current_user.is_authenticated})
    return response

def logout():
    logout_user()
    response = jsonify({
        "message": "You are now logged out"})
    return response