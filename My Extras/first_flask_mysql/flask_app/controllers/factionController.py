from flask_app import app
from flask import render_template,redirect,request,flash

from flask_app.models.friend import Friend
from flask_app.models.faction import Faction

@app.route("/faction/new")
def newFaction():
    return render_template("/addFaction.html")

@app.route("/faction/create", methods = ['POST'])
def createFaction():

    queryData = {
        "name" : request.form['name'],
        "level" : request.form['level'],
        "date_created" : request.form['date_created']
    }

    newFactionID = Faction.createNewFaction(queryData)
    return redirect("/")

@app.route("/faction/<int:faction_id>")
def showOneFaction(faction_id):

    queryData = {
        "faction_id" : faction_id
    }
    # one_friend = Friend.get_one_friend(query_data)
    oneFaction = Faction.getFactionWithFriends(queryData)

    return render_template("showOneFaction.html", oneFaction = oneFaction)