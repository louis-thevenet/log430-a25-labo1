= Rapport Labo 1 - LOG430 - Louis Thevenet

== Question 1

_Quelles commandes avez-vous utilisées pour effectuer les opérations UPDATE et DELETE dans MySQL ? Avez-vous uniquement utilisé Python ou également du SQL ? Veuillez inclure le code pour illustrer votre réponse._

J'ai utilisé les commandes SQL `UPDATE` et `DELETE`:

```python
def update(self, user):
    """ Update given user in MySQL """
    # If name exist, update email
    self.cursor.execute("SELECT 1 FROM users WHERE name=%s;",
                        (user.name, ))
    if self.cursor.fetchone():
        self.cursor.execute("UPDATE users SET email=%s WHERE name=%s;",
                            (user.email, user.name))
        self.conn.commit()
        return True

    # If email exist, update name
    self.cursor.execute("SELECT 1 FROM users WHERE email=%s;",
                        (user.email, ))
    if self.cursor.fetchone():
        self.cursor.execute("UPDATE users SET name=%s WHERE email=%s;",
                            (user.name, user.email))
        self.conn.commit()
        return True
    return False

def delete(self, user_id):
    """ Delete user from MySQL with given user ID """
    self.cursor.execute("DELETE FROM users WHERE id=%s", (user_id, ))
    self.conn.commit()
    if self.cursor.fetchone():
        return True
    return False
```

J'ai également ajouté ces actions dans l'application:

#image("./app_options.png")
== Question 2

_Quelles commandes avez-vous utilisées pour effectuer les opérations dans MongoDB ? Avez-vous uniquement utilisé Python ou également du SQL ? Veuillez inclure le code pour illustrer votre réponse._

MongoDB permet de n'utiliser que des commandes Python pour manipuler les données.

Initialisation:
```python
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

```

Et voici les différentes commandes:
```python
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

    def close(self):
        self.client.close()

```
