# Import function that will return an instance of a connection
from mysqlconnection import connectToMySQL

# model the class after the friend table from our database
class Friend:
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
        results = connectToMySQL('first_flask').query_db(query);
        # Create and empty list for our instances of friend
        friends=[];
        # iterate over the db results to make new instances of the friend class with the data from the db
        for friend in results:
            friends.append( cls(friend) )
        return friend;