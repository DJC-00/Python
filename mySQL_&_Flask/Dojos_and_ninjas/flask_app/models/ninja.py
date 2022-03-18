from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    db = 'dojos_and_ninjas_schema'
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def getAllNinjas(cls):
        query = "SELECT * FROM ninjas;"
        queryResults = connectToMySQL(cls.db).query_db(query)
        allNinjas = []

        for item in queryResults:
            allNinjas.append(cls(item))
        return allNinjas

    @classmethod
    def insertNewNinja(cls,data):
        query = """INSERT INTO ninjas ( first_name, last_name, age, created_at, updated_at, dojo_id)
                VALUES ( %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s );"""
        connectToMySQL(cls.db).query_db(query,data)

        return 

        # ** In case we want to reference the data within the calling function **
        # queryResults = connectToMySQL(cls.db).query_db(query,data)
        # return queryResults 
        

    @classmethod
    def getSingleNinja(cls,data):
        return