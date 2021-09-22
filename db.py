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

# Returns F if no matching username+password combo is found in database
def get_user_credentials(username, password):
    sql = "SELECT username, password FROM users WHERE username=:username AND password=:password"
    result = db.session.execute(sql, {"username":username, "password":password})
    return_list = result.fetchall()
    # Check if result is empty
    try: 
        if return_list[0][1] is not "":
            return True
    except:
        return False

# Fails if username already exists bc username is unique in db
def add_user(username, password):
    sql = "INSERT INTO users (username, admin, password) VALUES (:username, False, :password);"
    try: 
        db.session.execute(sql, {"username":username, "password":password})
        db.session.commit()
        return True
    except:
        return False
