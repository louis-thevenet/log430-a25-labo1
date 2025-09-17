import os
from dotenv import load_dotenv
import mysql.connector
from models.user import User
import pymongo
from bson.objectid import ObjectId


class UserDAOMongo:

    def __init__(self):
        try:
            env_path = ".env"
            print(os.path.abspath(env_path))
            load_dotenv(dotenv_path=env_path)
            db_host = os.getenv("MONGODB_HOST")
            db_user = os.getenv("DB_USERNAME")
            db_pass = os.getenv("DB_PASSWORD")
            self.client = pymongo.MongoClient(
                f"mongodb://{db_user}:{db_pass}@{db_host}/")
            self.users = self.client["admin"]["users"]
            if self.users is None:
                raise Exception("Erreur de connexion à la base de données")
        except FileNotFoundError as e:
            print("Attention : Veuillez créer un fichier .env")
        except Exception as e:
            print("Erreur : " + str(e))

    def select_all(self):
        """ Select all users from Mongo"""
        users = []
        for user in self.users.find():
            users.append(User(user["_id"], user["name"], user["email"]))
        return users

    def insert(self, user):
        """ Insert given user into Mongo"""
        result = self.users.insert_one({
            "name": user.name,
            "email": user.email,
        })
        return result.inserted_id

    def update(self, user):
        """Update user in Mongo. """
        if type(user.id) is str:
            id = ObjectId(user.id)
        else:
            id = user.id
        result = self.users.update_one(
            {"_id": id}, {"$set": {
                "email": user.email,
                "name": user.name,
            }})
        return result.matched_count > 0

    def delete(self, user_id):
        """ Delete user from Mongo with given user ID """
        if type(user_id) is str:
            id = ObjectId(user_id)
        else:
            id = user_id
        result = self.users.delete_one({"_id": id})
        print(result.deleted_count)
        return result.deleted_count > 0

    def delete_all(self):
        """ Empty users collection in Mongo """
        self.users.delete_many({})

    def close(self):
        self.client.close()
