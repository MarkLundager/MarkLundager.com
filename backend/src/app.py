from flask import Flask, render_template, jsonify
from datetime import datetime
from .user_routes import user_routes,login_manager
from flask_cors import CORS

#Global variables
app = Flask(__name__, static_folder='../../frontend/build/static', template_folder='../../frontend/build')
with open("key.txt", "r", encoding="utf-8") as file:
    key = file.read().strip()
app.config['SECRET_KEY'] = key
app.config['LOGIN_DISABLED'] = False
login_manager.init_app(app)
app.register_blueprint(user_routes)

CORS(app)
    

@app.route('/timeUntilCanada', methods=['GET'])
def timeUntilCanada():
    return calculate_time_remaining()


def calculate_time_remaining():
    # Get the current date and time
    current_datetime = datetime.now()

    # Set the target date (June 6th)
    target_date = datetime(current_datetime.year, 6, 6)

    # Calculate the time difference
    time_difference = target_date - current_datetime
    total_seconds_remaining = int(time_difference.total_seconds())

    # Extract days, hours, minutes, and seconds
    days_remaining = time_difference.days
    hours_remaining, remainder = divmod(time_difference.seconds, 3600)
    minutes_remaining, seconds_remaining = divmod(remainder, 60)

    # Display the time remaining
    print(f"Time remaining until June 6th: {days_remaining} days, {hours_remaining} hours, {minutes_remaining} minutes, {seconds_remaining} seconds")
    return jsonify({'days': days_remaining,
                    'hours': hours_remaining,
                    'minutes': minutes_remaining,
                    'seconds': seconds_remaining,
                    'totalSeconds': total_seconds_remaining
                    })



    # Implement a function to load the user from your database
    # Example: return User(user_id, username, authority)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
