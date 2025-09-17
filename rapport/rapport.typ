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
