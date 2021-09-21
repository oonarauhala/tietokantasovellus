from app import app
from flask import render_template

@app.route("/")
def index():
    areas = db.get_area()
    print(areas)
    return render_template("index.html", area1=areas[0][1], area2=areas[1][1])

@app.route("/area")
def area():
    dinosaurs = db.get_area_dinosaurs()
    return "Test"

@app.route("/admin")
def admin():
    return render_template("admin.html")

import db