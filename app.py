from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    sql = "SELECT * FROM areas;"
    result = db.session.execute(sql)
    area = result.fetchone()
    try: 
        return f"Area selected: {area[1]}"
    except:
        return render_template("index.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")