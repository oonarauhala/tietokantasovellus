from app import app
from flask import render_template

@app.route("/")
def index():
    areas = db.get_area()
    return render_template("index.html", area1=areas[0][1], area2=areas[1][1],
    area3=areas[2][1], area4=areas[3][1])

@app.route("/area1")
def area():
    dinosaurs = db.get_area_dinosaurs(1)
    return render_template("dino_area.html", dinosaurs=dinosaurs)

@app.route("/area2")
def area1():
    dinosaurs = db.get_area_dinosaurs(2)
    return render_template("dino_area.html", dinosaurs=dinosaurs)

@app.route("/area3")
def area2():
    dinosaurs = db.get_area_dinosaurs(3)
    return render_template("dino_area.html", dinosaurs=dinosaurs)

@app.route("/area4")
def area3():
    dinosaurs = db.get_area_dinosaurs(4)
    return render_template("dino_area.html", dinosaurs=dinosaurs)

@app.route("/admin")
def admin4():
    return render_template("admin.html")

import db