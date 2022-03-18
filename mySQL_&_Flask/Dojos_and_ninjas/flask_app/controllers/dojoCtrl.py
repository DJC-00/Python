from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def dojos():
    dojoList = Dojo.getAllDojos()
    return render_template("dojosHome.html", dojoList = dojoList)

@app.route("/dojo/<int:dojo_id>")
def showOneDojo(dojo_id):

    queryData = {
        "dojo_id" : dojo_id
    }

    dojoInfo = Dojo.getDojoWithNinjas(queryData)

    return render_template("showOneDojo.html", dojoInfo = dojoInfo)

@app.route("/dojo/create", methods = ['POST'])
def createNewDojo():
    queryData = {
        "name" : request.form["dojoName"]
    }

    newDojo = Dojo.createNewDojo(queryData)
    return redirect('/')
