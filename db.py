from sqlalchemy.orm import session
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
    sql = f"""SELECT TO_CHAR(f.date, 'YYYY.MM.HH'), TO_CHAR(f.time, 'HH24:MI'), d.id AS dinosaur_id, f.id AS time_id, f.available
              FROM feeding_times f, dinosaurs d 
              WHERE f.dinosaur = d.id;"""
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

# Does not check if there is an earlier reservation
def add_reservation(username, time_id):
    sql = f"""UPDATE users 
                    SET reserved_time = {time_id}
                    WHERE username = :username; 
              UPDATE feeding_times
                    SET available = available -1
                    WHERE id={time_id};"""
    db.session.execute(sql, {"username":username})
    db.session.commit()

def get_user_data(username):
    sql = f"""SELECT u.username, TO_CHAR(f.date, 'YYYY.MM.HH') AS date, TO_CHAR(f.time, 'HH24:MI') AS time 
              FROM users u LEFT JOIN feeding_times f 
              ON u.reserved_time=f.id 
              WHERE username=:username;"""
    result = db.session.execute(sql, {"username":username})
    return result.fetchall()

def get_feeding_time(id):
    sql = f"SELECT TO_CHAR(date, 'YYYY.MM.HH'), TO_CHAR(time, 'HH24:MI') FROM feeding_times WHERE id={id}"
    result = db.session.execute(sql)
    return result.fetchall()

# Update old feeding time availability in case user reserves a new one
def update_old_time(time_id):
    sql = f"UPDATE feeding_times SET available = available +1 WHERE id={time_id};"
    db.session.execute(sql)
    db.session.commit()

def get_user_reservation(username):
    sql = "SELECT reserved_time FROM users WHERE username=:username;"
    result = db.session.execute(sql, {"username":username})
    return result.fetchall()

def get_admin_status(username: str):
    sql = "SELECT admin FROM users WHERE username=:username;"
    result = db.session.execute(sql, {"username":username})
    return result.fetchone()
    
def get_dinosaur_names_ids():
    sql = "SELECT id, name FROM dinosaurs;"
    result = db.session.execute(sql)
    return result

def post_new_time(date, time, available, dinosaur_id):
    sql = "INSERT INTO feeding_times(date, time, available, dinosaur) VALUES (:date, :time, :available, :dinosaur_id);"
    db.session.execute(sql, {"date":date, "time":time, "available":available, "dinosaur_id":dinosaur_id})
    db.session.commit()

def get_all_times_for_edit():
    sql = "SELECT d.id AS dinosaur_id, f.id AS time_id, TO_CHAR(f.date, 'YYYY.MM.HH'), TO_CHAR(f.time, 'HH24:MI'), f.available FROM dinosaurs d, feeding_times f WHERE d.id=f.dinosaur;"
    result = db.session.execute(sql)
    return result