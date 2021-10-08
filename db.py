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
    sql = f"""SELECT TO_CHAR(f.date, 'YYYY.MM.DD'), TO_CHAR(f.time, 'HH24:MI'), d.id AS dinosaur_id, f.id AS time_id, f.available
              FROM feeding_times f, dinosaurs d 
              WHERE f.dinosaur = d.id;"""
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
    sql = f"""SELECT u.username, TO_CHAR(f.date, 'YYYY.MM.DD') AS date, TO_CHAR(f.time, 'HH24:MI') AS time 
              FROM users u LEFT JOIN feeding_times f 
              ON u.reserved_time=f.id 
              WHERE username=:username;"""
    result = db.session.execute(sql, {"username":username})
    return result.fetchall()

def get_feeding_time(id):
    sql = f"SELECT TO_CHAR(date, 'YYYY.MM.DD'), TO_CHAR(time, 'HH24:MI') FROM feeding_times WHERE id={id}"
    result = db.session.execute(sql)
    return result.fetchall()

# Update old feeding time availability in case user reserves a new one
def update_old_time(time_id):
    sql = f"UPDATE feeding_times SET available = available +1 WHERE id={time_id};"
    db.session.execute(sql)
    db.session.commit()

def get_user_reservation(username):
    sql = "SELECT TO_CHAR(f.date, 'YYYY.MM.DD'), TO_CHAR(f.time, 'HH24:MI') FROM feeding_times f, users u WHERE username=:username AND f.id=u.reserved_time;"
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
    sql = "SELECT d.id AS dinosaur_id, f.id AS time_id, TO_CHAR(f.date, 'YYYY.MM.DD') AS date, TO_CHAR(f.time, 'HH24:MI') AS time, f.available FROM dinosaurs d, feeding_times f WHERE d.id=f.dinosaur;"
    result = db.session.execute(sql)
    return result

def post_time_update(date, time, available, time_id):
    sql = """UPDATE feeding_times 
            SET date=:date, time=:time, available=:available
            WHERE id=:time_id"""
    db.session.execute(sql, {"date":date, "time":time, "available":available, "time_id":time_id})
    db.session.commit()

def delete_time(time_id):
    sql = "DELETE FROM feeding_times WHERE id=:time_id"
    db.session.execute(sql, {"time_id":time_id})
    db.session.commit()

def get_todays_times():
    sql = """SELECT TO_CHAR(f.date, 'YYYY.MM.DD') AS date, TO_CHAR(f.time, 'HH24:MI') AS time, d.name 
            FROM feeding_times f, dinosaurs d WHERE d.id=f.dinosaur AND f.date=CURRENT_DATE 
            ORDER BY date, time;"""
    return db.session.execute(sql)

def get_random_dino_info():
    sql = """SELECT d.id, d.name, d.description, a.name AS area FROM dinosaurs d, areas a 
            WHERE d.location=a.id 
            ORDER BY random() 
            LIMIT 5;"""
    return db.session.execute(sql)

def get_search_results_date(date: str):
    sql = f"""SELECT TO_CHAR(f.date, 'YYYY.MM.DD') AS date, TO_CHAR(f.time, 'HH24:MI') AS time, d.name 
            FROM feeding_times f, dinosaurs d 
            WHERE d.id=f.dinosaur AND date='{date}'::DATE;"""
    return db.session.execute(sql)

def get_search_results_text(text:str):
    text = text.lower()
    results = []
    # Search fields (dinosaurs.name, dinosaurs.description, areas.name) 
    # and return all matches
    sql = "SELECT name FROM dinosaurs WHERE LOWER(name) LIKE :text;"
    results.append(db.session.execute(sql, {"text":text}).fetchall())
    sql = "SELECT description FROM dinosaurs WHERE LOWER(description) LIKE :text;"
    results.append(db.session.execute(sql, {"text":f"%{text}%"}).fetchall())
    sql = "SELECT name FROM areas WHERE LOWER(name) LIKE :text;"
    results.append(db.session.execute(sql, {"text":text}).fetchall())
    return results
    