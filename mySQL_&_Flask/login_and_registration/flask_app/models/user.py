from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app import app
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 



class User:
    db = "login_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_register(rawFormData):
        isValid = True

        if len(rawFormData["first_name"]) < 2:
            flash("First name must be at least 2 characters long")
            isValid = False

        if len(rawFormData["last_name"]) < 2:
            flash("First name must be at least 2 characters long")
            isValid = False

        if len(rawFormData["password"]) < 2:
            flash("First name must be at least 2 characters long")
            isValid = False

        if rawFormData["password"] != rawFormData["password_Confirm"] < 2:
            flash("passwords do no match")
            isValid = False

        if not EMAIL_REGEX.match(rawFormData["email"]):
            flash("Please enter a valid Email Address")
            isValid = False
        
        return isValid

    @staticmethod
    def validate_login(rawFormData):
        # data = { "email" : request.form["email"] }
        isValid = True
        userFromDB = User.getByEmail(rawFormData)
        # print(f"+=+=+=+=+=+=\n{rawFormData['password']}\n+=+=+=+=+=+=\n{userFromDB.password}\n+=+=+=+=+=+=")
        if not userFromDB:
            flash("Invalid Email or Password")
            isValid = False
        elif not Bcrypt.check_password_hash(User, userFromDB.password , rawFormData['password']):
            print(Bcrypt.check_password_hash(User, userFromDB.password , rawFormData['password']))
            flash("Invalid Email or Password")
            isValid = False

        
        return isValid

    @classmethod
    def createNewUser(cls,data):
        query = """INSERT INTO USERS (first_name, last_name, email, password, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW() );"""

        queryResult = connectToMySQL(cls.db).query_db(query,data)
        return queryResult
        
    @classmethod
    def getByEmail(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False

        return cls(result[0])
    
    @classmethod
    def getByUserID(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False

        return cls(result[0])