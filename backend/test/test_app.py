import pytest
import os
import sqlite3

current_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(current_directory, 'db.db')
db = sqlite3.connect(database_path)

def main():
    create_Mark_user()
    see_db_users()


def see_db_users():
    c = db.cursor()
    c.execute("""
                SELECT id, username, email, authority
                FROM accounts 
                """)
    rows = c.fetchall()

    for row in rows:
        print(row)
    c.close()

def create_Mark_user():
    c = db.cursor()
    c.execute("""
                INSERT INTO accounts (id, username, email, authority, password_hash)
                VALUES (0, 'MurkBurkWurk', 'mark_06_20@outlook.com', 5, 'hashed_password');
                """)
    c.close()

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()