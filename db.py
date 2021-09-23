from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

def get_area():
    sql = "SELECT * FROM areas;"
    result = db.session.execute(sql)
    return result.fetchall()

def get_area_dinosaurs(area):
    # No security problem in sql since area is not user input
    sql = f"SELECT * FROM dinosaurs WHERE location = {area}"
    result = db.session.execute(sql)
    return result.fetchall()

def get_all_feeding_times():
    sql = f"SELECT TO_CHAR(f.date, 'YYYY:MM:HH'), TO_CHAR(f.time, 'HH24:MI'), d.id FROM feeding_times f, dinosaurs d WHERE f.dinosaur = d.id;"
    result = db.session.execute(sql)
    return result.fetchall()    

# Not in use atm
def get_dino_feeding_times(dinosaur_id):
    # No security problem since dinosaur_id is not user input
    sql = f"SELECT TO_CHAR(date, 'YYYY:MM:HH'), TO_CHAR(time, 'HH24:MI') FROM feeding_times WHERE dinosaur = {dinosaur_id};"
    result = db.session.execute(sql)
    return result.fetchall()

def get_user_credentials(username):
    sql = "SELECT username, password FROM users WHERE username=:username;"
    result = db.session.execute(sql, {"username":username})
    return result.fetchall()

# Fails if username already exists bc username is unique in db
def add_user(username, password):
    sql = "INSERT INTO users (username, admin, password) VALUES (:username, False, :password);"
    try: 
        db.session.execute(sql, {"username":username, "password":password})
        db.session.commit()
        return True
    except:
        return False
