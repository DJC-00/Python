# Import function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the friend table from our database
class Friend:
    db = "first_flask"
    def __init__(self, data):
        self.id = data['id'];
        self.first_name = data['first_name'];
        self.last_name = data['last_name'];
        self.occupation = data['occupation'];
        self.age = data['age'];
        self.created_at = data['created_at'];
        self.updated_at = data['updated_at'];

    # Use the class method to query the database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends";
        # Call the connectToMySQL function with the schema you are targeting
        results = connectToMySQL(cls.db).query_db(query);
        # Create and empty list for our instances of friend
        friends=[];
        # iterate over the db results to make new instances of the friend class with the data from the db
        for friend in results:
            friends.append( cls(friend) );
        return friends;

    @classmethod
    def get_one_friend(cls,data):
        query = "SELECT * FROM friends WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data);
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL(cls.db).query_db( query, data )
        return result