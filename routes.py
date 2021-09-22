#from werkzeug.wrappers import request
from operator import add
from os import umask
from werkzeug.wrappers import request
from app import app
from flask import render_template, request, session, redirect

@app.route("/")
def index():
    areas = db.get_area()
    return render_template("index.html", area1=areas[0][1], area2=areas[1][1],
    area3=areas[2][1], area4=areas[3][1])

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login_result", methods=["POST"])
def login_result():
    username = request.form["username"]
    password = request.form["password"]
    result = db.get_user_credentials(username, password)
    if result:
        return "Login successful"
    return "Login failed"

@app.route("/register_result", methods=["POST"])
def register_result():
    # TODO password = password hash
    username = request.form["username_reg"]
    password = request.form["password_reg"]
    add_user_result = db.add_user(username, password)
    if add_user_result:
        return "User added!"
    return "Jotain meni pieleen"

@app.route("/area1")
def area1():
    dinosaurs = db.get_area_dinosaurs(1)
    return render_template("dino_area.html", dinosaurs=dinosaurs)

@app.route("/area2")
def area2():
    dinosaurs = db.get_area_dinosaurs(2)
    return render_template("dino_area.html", dinosaurs=dinosaurs)

@app.route("/area3")
def area3():
    dinosaurs = db.get_area_dinosaurs(3)
    return render_template("dino_area.html", dinosaurs=dinosaurs)

@app.route("/area4")
def area4():
    dinosaurs = db.get_area_dinosaurs(4)
    return render_template("dino_area.html", dinosaurs=dinosaurs)

@app.route("/admin")
def admin():
    return render_template("admin.html")

import db, login