import sqlite3
import bcrypt
from flask_login import UserMixin, login_user,logout_user
from flask import jsonify
def setup_user_manager(app, login_manager):
    login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, user_id, username, authority):
        self.id = user_id
        self.username = username
        self.authority = authority

def sign_up(db, username, email, password):
    with db.cursor() as c:
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

def sign_in(db, username_or_email, password):
    with db.cursor() as c:
        c.execute("""
                SELECT id, username, email, password, authority
                FROM accounts
                WHERE username = ? OR email = ? 
                """,
                (username_or_email, username_or_email)
                )
        user_data = c.fetchone()
        if user_data:
            stored_password = user_data[3]
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                response = jsonify({"message": "Login successful"})
                response.status_code = 200
                user = User(user_data[0], user_data[1], user_data[4])
                login_user(user)
                return response
            else:
                response = jsonify({"error": "Invalid password"})
                response.status_code = 401
                return response
        else:
            response = jsonify({"error": "User not found"})
            response.status_code = 404
            return response

def get_user(db, user_id):
    with db.cursor() as c:
        c.execute("""
                SELECT id, username, authority
                FROM accounts
                WHERE id = ? 
                """,
                (user_id)
                )
        user_data = c.fetchone()
        if user_data:
            user = User(user_data[0], user_data[1],user_data[2])
            return user
        else:
            return None
        
def logout():
    logout_user()
    return "you are now logged out."