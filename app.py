from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "DinoPark"

@app.route("/admin")
def admin():
    return "Admin page for admins to do admin stuff :)"