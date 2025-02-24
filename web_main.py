from flask import Flask, render_template, jsonify
from wakeonlan import send_magic_packet
import json


app = Flask(__name__)

@app.route("/")  # index
def index():
    return render_template("index.html")

@app.route("/functions/wol/<device_name>", methods=["GET"])
def wol(device_name):
    try:
        with open("./config/devices.json", "r") as f:
            devices = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return jsonify({"error": "Internal server error: Could not load configuration"}), 500

    if device_name in devices:
        try:
            send_magic_packet(devices[device_name])
            return jsonify({"message": f"Magic packet sent to {device_name}. Waking up..."}), 200
        except Exception as e:
            return jsonify({"error": f"Exception occurred: {str(e)}"}), 500
    else:
        return jsonify({"error": f"Device '{device_name}' not found. Try another."}), 404


@app.route("/user/greet/<username>", methods=["GET"])  # example for dynamic routes
def show_user(username):
    return f"Hello, {username}"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)