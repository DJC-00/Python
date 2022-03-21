# Import function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import friend
# model the class after the friend table from our database
class Faction:
    db = "first_flask"
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.level = data["level"]
        self.dateCreated = data["date_created"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.factionMembers = [] #placeholder for list of friends
    


    @classmethod
    def createNewFaction(cls,data):
        query = "INSERT INTO factions (name, level, date_created, created_at, updated_at ) VALUES ( %(name)s , %(level)s , %(date_created)s , NOW() , NOW() );"
        queryResult = connectToMySQL(cls.db).query_db(query, data)
        return queryResult

    @classmethod
    def getAllFactions(cls):
        query = "SELECT id, name, level, DATE_FORMAT(date_created, '%M %d, %Y') AS date_created, created_at, updated_at FROM factions;"
        #"SELECT id, name, level, DATE_FORMAT(date_created, '%M %d, %Y') AS date_created, created_at, updated_at FROM factions;"
        queryResults = connectToMySQL(cls.db).query_db(query)

        allFactions = []

        for each in queryResults:
            allFactions.append( cls(each) )
        return allFactions

    @classmethod
    def getFactionWithFriends(cls,data):
        query = """SELECT * FROM factions
                JOIN friends ON factions.id = friends.factions_id
                WHERE factions.id = %(faction_id)s;"""

        queryResults = connectToMySQL(cls.db).query_db(query,data)

        faction = cls(queryResults[0])

        for element in queryResults:
            friendData= {
                "id" : element['friends.id'],
                "first_name" : element['first_name'],
                "last_name" : element['last_name'],
                "occupation" : element['occupation'],
                "age" : element['age'],
                "created_at" : element['friends.created_at'],
                "updated_at" : element['friends.updated_at']
            }

            friendInstance = friend.Friend(friendData)
            faction.factionMembers.append(friendInstance)

        return faction