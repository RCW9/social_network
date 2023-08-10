from lib.user import User

class UserRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from users ORDER By id ASC')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["email"])
            users.append(item)
        return users

    # Find a single artist by their id
    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["id"], row["username"], row["email"])

    
    def create(self, user):
        self._connection.execute('INSERT INTO users(username, email) VALUES (%s, %s)', [
                    user.username, user.email])

    
    def delete(self, user_id):
        self._connection.execute(
            'DELETE FROM users WHERE id = %s', [user_id])
        

    def update_email(self, user):
        self._connection.execute(
            'UPDATE users SET email = %s WHERE id = %s', [user.email, user.id])