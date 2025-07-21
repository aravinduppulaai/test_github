import logging
from datetime import datetime
import os
from flask import Flask, jsonify, request

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

# Create a log file with the current date and time
log_filename = datetime.now().strftime('logs/log_%Y-%m-%d_%H-%M-%S.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

current_user = None

def login(username, password):
    global current_user
    if username and password:
        current_user = username
        logging.info(f"Logged in as {username}")
        print(f"Logged in as {username}")
        return True
    else:
        logging.warning("Username and password required.")
        print("Username and password required.")
        return False

def logout():
    global current_user
    if current_user:
        logging.info(f"User {current_user} logged out.")
        print(f"User {current_user} logged out.")
        current_user = None
    else:
        logging.warning("No user is currently logged in.")
        print("No user is currently logged in.")

def show_user_details():
    if current_user:
        logging.info(f"Current user: {current_user}")
        print(f"Current user: {current_user}")
    else:
        logging.info("No user is currently logged in.")
        print("No user is currently logged in.")

def run():
    print("App is running! Use the main.py CLI to login, logout, or view user details.")

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, world!"})

@app.route('/login', methods=['POST'])
def api_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if login(username, password):
        return jsonify({"success": True, "message": f"Logged in as {username}"})
    else:
        return jsonify({"success": False, "message": "Username and password required."}), 400

@app.route('/logout', methods=['POST'])
def api_logout():
    global current_user
    if current_user:
        user = current_user
        logout()
        return jsonify({"success": True, "message": f"User {user} logged out."})
    else:
        return jsonify({"success": False, "message": "No user is currently logged in."}), 400

@app.route('/user', methods=['GET'])
def api_user():
    if current_user:
        return jsonify({"user": current_user})
    else:
        return jsonify({"user": None, "message": "No user is currently logged in."}) 