from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    area = db.get_area()
    print(area)
    return render_template("index.html", area1=area[0][1], area2=area[1][1])
    
@app.route("/admin")
def admin():
    return render_template("admin.html")

import db