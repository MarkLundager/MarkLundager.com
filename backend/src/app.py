from flask import Flask, render_template, jsonify
from datetime import datetime
from .user_routes import user_routes,login_manager
from flask_cors import CORS

#Global variables
app = Flask(__name__, static_folder='../../frontend/build/static', template_folder='../../frontend/build')

keyfile = open("backend/src/key.txt")
key = keyfile.read().strip()
keyfile.close()
app.config['SECRET_KEY'] = key
app.config['LOGIN_DISABLED'] = False
login_manager.init_app(app)
app.register_blueprint(user_routes)

CORS(app)
    

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
