# Import function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import faction
# model the class after the friend table from our database
class Friend:
    db = "first_flask"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.faction = {}

    # Use the class method to query the database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # Call the connectToMySQL function with the schema you are targeting
        results = connectToMySQL(cls.db).query_db(query)
        # Create and empty list for our instances of friend
        friends=[]
        # iterate over the db results to make new instances of the friend class with the data from the db
        for friend in results:
            friends.append( cls(friend) )
        return friends

    @classmethod
    def get_one_friend(cls,data):
        query = "SELECT * FROM friends WHERE id = %(id)s;"
        queryResult = connectToMySQL(cls.db).query_db(query, data)
        return cls(queryResult[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at, factions_id) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW(), %(faction)s );"
        # data is a dictionary that will be passed into the save method from server.py
        queryResult = connectToMySQL(cls.db).query_db( query, data )
        return queryResult

    @classmethod
    def getFriendWithFaction(cls, data):
        query = """SELECT * FROM friends
                JOIN factions ON friends.factions_id = factions.id
                WHERE friends.id = %(id)s;"""

        queryResult = connectToMySQL(cls.db).query_db(query,data)

        friend = cls(queryResult[0]) #Create friend instance

        factionData = {
            "id" : queryResult[0]["factions.id"],
            "name" : queryResult[0]["name"], # Do not use factions.[var] for non coliding fields
            "level" : queryResult[0]["level"],
            "date_created" : queryResult[0]["date_created"],
            "created_at" : queryResult[0]["factions.created_at"],
            "updated_at" : queryResult[0]["factions.updated_at"]
        }

        factionInstance = faction.Faction(factionData)

        friend.faction = factionInstance

        return friend







# class Friend:
#     db = "first_flask"
#     def __init__(self, data):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.occupation = data['occupation']
#         self.age = data['age']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
#         self.factionName = data['faction_name']

#     # Use the class method to query the database
#     @classmethod
#     def get_all(cls):
#         query = "SELECT friends.id, friends.first_name, friends.last_name, friends.occupation, friends.age, friends.created_at, friends.updated_at, factions.name AS faction_name FROM factions RIGHT JOIN friends ON factions.id = friends.factions_id;"
#         # Call the connectToMySQL function with the schema you are targeting
#         results = connectToMySQL(cls.db).query_db(query)
#         # Create and empty list for our instances of friend
#         friends=[]
#         # iterate over the db results to make new instances of the friend class with the data from the db
#         for friend in results:
#             friends.append( cls(friend) )
#         return friends