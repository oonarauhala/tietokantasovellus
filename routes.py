from os import abort
import secrets
from werkzeug.wrappers import request
from werkzeug.security import check_password_hash, generate_password_hash
from flask import render_template, request, session, redirect
from secrets import token_hex
from app import app


@app.route("/")
def index():
    areas = users.get_area()
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
    user_data = users.get_user_data(session["username"])
    return render_template("profile.html", user_data=user_data)

@app.route("/login_result", methods=["POST"])
def login_result():
    username = request.form["username"]
    password = request.form["password"]
    result = users.get_user_credentials(username)
    if not result:
        # Login failed: no username
        # TODO: display msg
        return redirect("/login")
    if check_password_hash(result[0][1], password):
        # Login successful
        session["username"] = username
        # Load possible reservation to session
        time = users.get_user_reservation(username)
        # Add session csrf_token
        session["csrf_token"] = secrets.token_hex(16)
        try:
            # time[0][0] = date, time[0][1] = time
            session["time"] = (time[0][0], time[0][1])
        except:
            # No previous reservation
            pass
        return redirect("/")
    # Login failed: wrong password
    # TODO: display msg
    return redirect("/login")

@app.route("/register_result", methods=["POST"])
def register_result():
    username = request.form["username_reg"]
    password = request.form["password_reg"]
    if validator.validate_string(username) and validator.validate_string(password):
        password_hash = generate_password_hash(password)
        add_user_result = users.add_user(username, password_hash)
        if add_user_result:
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        # TODO: display msg
    return redirect("/login")

@app.route("/area<int:id>")
def area(id):
    dinosaurs = users.get_area_dinosaurs(id)
    times = users.get_all_feeding_times()
    try:
        # User has a reserved time
        return render_template("dino_area.html", dinosaurs=dinosaurs, times=times,
            user_time=session["time"])
    except:
        return render_template("dino_area.html", dinosaurs=dinosaurs, times=times)

@app.route("/reserve_result", methods=["POST"])
def reserve_result():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    # Update users if user has an earlier reservation
    old_time_id = users.get_user_reservation(session["username"])
    try:
        users.update_old_time(old_time_id[0][0])
    except:
        pass
    try:
        time_id = request.form["feeding_time"]
        users.add_reservation(session["username"], time_id)
        time = users.get_feeding_time(time_id)
        session["time"] = (time[0][0], time[0][1])
        return redirect("/profile")
    except:
        return redirect("/")

@app.route("/admin")
def admin():
    dinosaurs = users.get_dinosaur_names_ids()
    dinosaurs=list(dinosaurs)
    times = list(users.get_all_times_for_edit())
    try:
        admin_status = users.get_admin_status(session["username"])[0]
        if admin_status:
            return render_template("admin.html", dinosaurs=dinosaurs, times=times)
        return redirect("/login_admin")
    except:
        return redirect("/login_admin")

@app.route("/login_admin")
def login_admin():
    return render_template("admin_login.html")

@app.route("/login_result_admin", methods=["POST"])
def login_result_admin():
    username = request.form["username"]
    password = request.form["password"]
    result = users.get_user_credentials(username)
    if not result:
        # Login failed: no username
        return redirect("/login_admin")
    if check_password_hash(result[0][1], password):
        # Login successful
        session["username"] = username
        session["csrf_token"] = secrets.token_hex(16)
    return redirect("/admin")

@app.route("/add_time", methods=["POST"])
def add_time():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    date = request.form["date"]
    time = request.form["time"]
    available = request.form["available"]
    dinosaur_id = request.form["dinosaur_id"]
    users.post_new_time(date, time, available, dinosaur_id)
    return redirect("/admin")

@app.route("/update_time", methods=["POST"])
def update_time():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    date = request.form["date"]
    time = request.form["time"]
    available = request.form["available"]
    dinosaur_id = request.form["dinosaur_id"]
    time_id = request.form[str(dinosaur_id)]
    users.post_time_update(date, time, available, time_id)
    return redirect("/admin")

@app.route("/delete_time", methods=["POST"])
def delete_time():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    dinosaur_id = request.form["dinosaur_id"]
    time_id = request.form[str(dinosaur_id)]
    users.delete_time(time_id)
    return redirect("/admin")

@app.route("/search")
def search():
    times = list(users.get_todays_times())
    dinosaurs = list(users.get_random_dino_info())
    return render_template("search.html", times=times, dinosaurs=dinosaurs)

@app.route("/search_result", methods=["POST"])
def search_result():
    try:
        date = request.form["search_date"]
        result_dates= list(users.get_search_results_date(date))
        return render_template("/search_result.html", times=result_dates)
    except:
        pass
    try:
        text = request.form["search_text"]
        if text == "":
            return redirect("/search")
        text_result = list(users.get_search_results_text(text))
        # Check if result is not empty
        counter = 0
        for result_list in text_result:
            if len(result_list) == 0:
                counter += 1
            if counter == 3:
                return redirect("/search")
        return render_template("/search_result.html", text_results=text_result)
    except:
        pass
    return redirect("/search")

import users, validator
