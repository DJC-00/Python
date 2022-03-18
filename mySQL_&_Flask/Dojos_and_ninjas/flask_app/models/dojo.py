from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.dojoNinjas = []

    @classmethod
    def getAllDojos(cls):
        query = "SELECT * FROM dojos;"
        queryResults = connectToMySQL(cls.db).query_db(query)
        allDojos = []

        for item in queryResults:
            allDojos.append(cls(item))
        return allDojos

    @classmethod
    def getDojoWithNinjas(cls):
        return

    @classmethod
    def createNewDojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW() );"
        queryResult = connectToMySQL(cls.db).query_db(query, data)
        return queryResult

    @classmethod
    def getDojoWithNinjas(cls,data):
        query = """SELECT * FROM dojos
                LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
                WHERE dojos.id = %(dojo_id)s;"""

        queryResults = connectToMySQL(cls.db).query_db(query,data)

        dojo = cls(queryResults[0])

        for item in queryResults:
            ninjaData= {
                "id" : item['ninjas.id'],
                "first_name" : item['first_name'],
                "last_name" : item['last_name'],
                "age" : item['age'],
                "created_at" : item['ninjas.created_at'],
                "updated_at" : item['ninjas.updated_at']
            }

            ninjaInstance = ninja.Ninja(ninjaData)
            print(ninjaInstance.first_name)
            print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            dojo.dojoNinjas.append(ninjaInstance)

    

        return dojo