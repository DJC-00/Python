from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "user_schema"
    def __init__(self, data):
        self.id = data['id'];
        self.firstName = data['first_name'];
        self.lastName = data['last_name'];
        self.email = data['email'];
        self.createdAt = data['created_at'];
        self.updatedAt = data['updated_at'];

    @classmethod
    def getAll(cls):
        # pre constructed query string
        query = "SELECT * FROM users"
        # Query DB and store results in "results"
        queryResults = connectToMySQL(cls.db).query_db(query);
        # Create a list to store users
        allUsers = []
        # From each unique result, use the data to create an instance of the user class and store that in the list of users
        for user in queryResults:
            allUsers.append( cls(user) )
        return allUsers
    
    @classmethod
    def createUser(cls,data):
        query = "INSERT INTO users ( first_name, last_name, email, created_at, updated_at) VALUES ( %(firstName)s,%(lastName)s,%(email)s,NOW(),NOW() );"
        queryResults = connectToMySQL(cls.db).query_db(query,data)
        return queryResults

    @classmethod
    def getOneUser(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        queryResult = connectToMySQL(cls.db).query_db(query,data)
        return cls(queryResult[0])

    @classmethod
    def confirmEdit(cls,data):
        query = "UPDATE users SET first_name = %(firstName)s, last_name = %(lastName)s, email = %(email)s WHERE id = %(id)s;"
        queryResult = connectToMySQL(cls.db).query_db(query,data)
        return queryResult

    @classmethod
    def deleteUser(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        queryResult = connectToMySQL(cls.db).query_db(query,data)
        return queryResult