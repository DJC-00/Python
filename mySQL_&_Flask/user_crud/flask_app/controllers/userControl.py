# burgers.py
from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.user import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/viewUsers")
def viewUser():
    allUsers = User.getAll();
    return render_template("viewUsers.html", allUsers = allUsers)

@app.route("/addUser")
def addUser():
    return render_template("addUser.html")

@app.route("/createNewUser", methods=['POST'])
def createNewUser():
    data = {
        "firstName": request.form["firstName"],
        "lastName": request.form["lastName"],
        "email": request.form["email"]
    }
    print(data)
    User.createUser(data);
    return redirect("/viewUsers")