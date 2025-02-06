from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")  # index
def index():
    return "<p>index</p>"

@app.route("/login")  # login
def login():
    return "<p>login</p>"

@app.route("/functions/wol/<device_name>")
def wol(device_name):
    return f"Waking up {device_name}"

@app.route("/user/<username>")  # example for dynamic routes
def show_user(username):
    return f"Hello, {username}"

app.run(host="127.0.0.1", port=8080, debug=True)