from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    area = db.get_area()
    try: 
        return f"Area selected: {area[1]}"
    except:
        return render_template("index.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

import db