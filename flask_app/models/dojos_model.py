from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas_model

class Dojo:
    # constant with db name
    DB = "dojos_and_ninjas_schema"
    def __init__(self, data):

        # map columns from table to attributes
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        # empty list to hold associated Ninja instances
        self.ninjas = []

    # CREATE
    @classmethod
    def save(cls, data):

        # insert query
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW())"

        # return id of new dojos row
        return connectToMySQL(cls.DB).query_db(query,data)



    # READ  
    @classmethod
    def get_all(cls):

        # select query
        query = "SELECT * FROM dojos"

        # list of dictionaries
        results = connectToMySQL(cls.DB).query_db(query)

        # create a list a Dojo instances
        dojos = []
        for result in results:
            dojos.append(cls(result))
        
        return dojos
    
    @classmethod
    def get_dojo_with_ninjas(cls,id):

        # make a dict with the id of the dojo we are looking for
        data = {
            "id" : id
        }

        # select query for all ninjas within a dojo
        query = """
            SELECT * FROM dojos 
            LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id 
            WHERE dojos.id = %(id)s"""

        results = connectToMySQL(cls.DB).query_db(query, data)

        # make a Dojo instance
        dojo = cls(results[0])

        # loop through results to add Ninja instances to the dojo.ninjas list
        for row in results:

            # format data to add Ninja instance
            ninja_data = {
                "id" : row["ninjas.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "age" : row["age"],
                "created_at" : row["ninjas.created_at"],
                "updated_at" : row["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninjas_model.Ninja(ninja_data))

        return dojo
