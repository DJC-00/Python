from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninja/create")
def createNewNinja():
    allDojos = Dojo.getAllDojos()
    return render_template('/createNewNinja.html', dojoList = allDojos)

@app.route("/ninja/create/confirm", methods=['POST'])
def insertNewNinja():
    queryData = {
        "first_name" : request.form["ninjaFirstName"],
        "last_name" : request.form["ninjaLastName"],
        "age" : request.form["ninjaAge"],
        "dojo_id" : request.form["dojoID"]
    }

    Ninja.insertNewNinja(queryData)
    return redirect("/")

    # or to save the result of the query
    #newNinja = Ninja.insertNewNinja(queryData)