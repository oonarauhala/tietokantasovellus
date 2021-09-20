from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    area = db.get_area()
    print(area)
    return render_template("index.html", areas=area)

@app.route("/admin")
def admin():
    return render_template("admin.html")

import db