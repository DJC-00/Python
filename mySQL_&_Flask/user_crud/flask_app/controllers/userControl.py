# burgers.py
from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.user import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/viewUsers")
def viewUsers():
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

@app.route("/viewSingleUser/<int:userID>")
def viewSingleUser(userID):

    data = {
        "id" : userID
    }
    # one_friend = Friend.get_one_friend(query_data)
    selectedUser = User.getOneUser(data)

    return render_template("singleUserInfo.html", selectedUser = selectedUser)

@app.route("/editUser/<int:userID>")
def editUser(userID):

    data = {
        "id" : userID
    }
    # one_friend = Friend.get_one_friend(query_data)
    #User.confirmEdit(data)
    selectedUser = User.getOneUser(data)
    return render_template("/editUser.html", selectedUser = selectedUser)

@app.route("/confirmEdit", methods=['POST'])
def confirmEdit():

    data = {
        "id" : request.form["id"],
        "firstName": request.form["firstName"],
        "lastName": request.form["lastName"],
        "email": request.form["email"]
    }
    # one_friend = Friend.get_one_friend(query_data)
    #User.confirmEdit(data)
    User.confirmEdit(data)
    return redirect("/viewSingleUser/" + str(data['id']))

@app.route("/deleteUser/<int:userID>")
def deleteUser(userID):
    
    data = {
        "id" : userID
    }
    # one_friend = Friend.get_one_friend(query_data)
    #User.confirmEdit(data)
    User.deleteUser(data)
    return redirect("/viewUsers")
