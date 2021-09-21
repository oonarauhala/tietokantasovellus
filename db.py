from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

def get_area():
    sql = "SELECT * FROM areas;"
    result = db.session.execute(sql)
    return result.fetchall()

def get_area2_dinosaurs():
    sql = "SELECT * FROM dinosaurs WHERE location = 2"
    result = db.session.execute(sql)
    return result.fetchall()
    