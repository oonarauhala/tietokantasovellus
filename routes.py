from werkzeug.wrappers import request
from werkzeug.security import check_password_hash, generate_password_hash
from app import app
from flask import render_template, request, session, redirect


@app.route("/")
def index():
    areas = db.get_area()
    return render_template("index.html", area1=areas[0][1], area2=areas[1][1],
    area3=areas[2][1], area4=areas[3][1])

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/profile")
def profile():
    user_data = db.get_user_data(session["username"])
    print(user_data)
    return render_template("profile.html", user_data=user_data)

@app.route("/login_result", methods=["POST"])
def login_result():
    username = request.form["username"]
    password = request.form["password"]
    result = db.get_user_credentials(username)
    print(result)
    if not result:
        # Login failed: no username
        # TODO: display msg
        return redirect("/login")
    if check_password_hash(result[0][1], password):
        # Login successful
        session["username"] = username
        # Load possible reservation to session
        time = db.get_user_reservation(username)
        if time[0][0] != None:
            session["time"] = (time[0][0], time[0][1])
        return redirect("/")
    # Login failed: wrong password
    # TODO: display msg
    return redirect("/login")

@app.route("/register_result", methods=["POST"])
def register_result():
    username = request.form["username_reg"]
    password = request.form["password_reg"]
    password_hash = generate_password_hash(password)
    add_user_result = db.add_user(username, password_hash)
    if add_user_result:
        session["username"] = username
        return redirect("/")
    # TODO: display msg
    return redirect("/login")

@app.route("/area<int:id>")
def area(id):
    dinosaurs = db.get_area_dinosaurs(id)
    times = db.get_all_feeding_times()
    try:
        # User has a reserved time
        return render_template("dino_area.html", dinosaurs=dinosaurs, times=times, user_time=session["time"])
    except:
        return render_template("dino_area.html", dinosaurs=dinosaurs, times=times)

@app.route("/reserve_result", methods=["POST"])
def reserve_result():
    # Update db if user has an earlier reservation
    old_time_id = db.get_user_reservation(session["username"])
    print(old_time_id[0][0])
    if old_time_id[0][0] is not None:
        db.update_old_time(old_time_id[0][0])
    # Update reservation to db
    time_id = request.form["feeding_time"]
    db.add_reservation(session["username"], time_id)
    time = db.get_feeding_time(time_id)
    session["time"] = (time[0][0], time[0][1])
    return redirect("/profile")

@app.route("/admin")
def admin():
    return render_template("admin.html")

import db