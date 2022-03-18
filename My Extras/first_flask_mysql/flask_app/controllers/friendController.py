from flask_app import app
from flask import render_template,redirect,request

from flask_app.models.friend import Friend
from flask_app.models.faction import Faction

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    allFriends = Friend.get_all()
    allFactions = Faction.getAllFactions()
    # allFactions = Faction.getAllFactions()
    print(allFriends)
    return render_template("index.html", friendList = allFriends, factionList = allFactions)

@app.route("/friend/<int:friend_id>")
def one_friend(friend_id):

    query_data = {
        "id" : friend_id
    }
    # one_friend = Friend.get_one_friend(query_data)
    one_friend = Friend.getFriendWithFaction(query_data)

    return render_template("show_friend.html", one_friend = one_friend)

@app.route('/addFriend')
def add_friend():
    allFactions = Faction.getAllFactions()
    return render_template('addFriend.html', factionList = allFactions)

@app.route('/createFriend', methods=["POST"])
def createFriend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"],
        "faction" : request.form["faction"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    newFriend = Friend.save(data)
    # Don't forget to redirect after saving to the database.
    # return redirect(f'/friend/{newFriend}')
    return redirect(f'/')
