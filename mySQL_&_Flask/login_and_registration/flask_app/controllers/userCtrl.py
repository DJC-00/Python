from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def userLanding():
    if "user_id" not in session:
        flash("Please login or register before entering site!")
        error = "error"
        return render_template("index.html", error = error)
    user_id = session["user_id"]
    # user_email = session["email"]
    # query_data = {
    #     "email" : user_email
    # }
    query_data = {
        "id" : user_id
    }
    current_user = User.getByUserID(query_data)
    return render_template("/dashboard.html", current_user = current_user)

# Register Route

@app.route("/register", methods = ["POST"])
def registerNewUser():
########################
# 1- Validate form info
#
# 2 - collect data from form, encrypt password
#
# 3 - run query to database with SQL Insert Query
#
# 4 - redirect to a different page
######################################################


    #1
    if not User.validate_register(request.form):
        print("error")
        return render_template("index.html", error = 'regFail')

    #2
    passHash = bcrypt.generate_password_hash(request.form["password"])
    queryData = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : passHash
    }

    #3
    new_user_id = User.createNewUser(queryData)
    session["user_id"] = new_user_id;

    #4
    return redirect("/")

@app.route("/login", methods = ["POST"])
def login():

    # 1. Validate login info
    if not User.validate_login(request.form):
        return render_template("index.html", error = 'loginFail')
        # return redirect("/")
    
    query_data = {
        "email" : request.form["email"]
    }

    currentUser = User.getByEmail(query_data)
    session["user_id"] = currentUser.id
    # session["email"] = currentUser.email

    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear();
    return redirect("/")