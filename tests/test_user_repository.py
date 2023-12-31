from lib.user_repository import UserRepository
from lib.user import User

"""
When we call UserRepository#all
We get a list of User objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new UserRepository

    result = repository.all() # Get all Users

    # Assert on the results
    assert result == [
        User(1, 'Pixies', 'pixie@msn'),
        User(2, 'Dixies', 'dixie@msn'),
        User(3, 'Lixies', 'lixie@msn'),
        User(4, 'Tixies', 'tixie@msn'),
    ]

"""
When we call UserRepository#find
We get a single User object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    user = repository.find(3)
    assert user == User(3, 'Lixies', 'lixie@msn')

"""
When we call UserRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, "Mixies", "Mixie@msn"))

    result = repository.all()
    assert result == [
        User(1, 'Pixies', 'pixie@msn'),
        User(2, 'Dixies', 'dixie@msn'),
        User(3, 'Lixies', 'lixie@msn'),
        User(4, 'Tixies', 'tixie@msn'),
        User(5, "Mixies", "Mixie@msn")
    ]
        


"""
When we call UserRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.delete(2)
    result = repository.all()
    assert result == [
        User(1, 'Pixies', 'pixie@msn'),
        User(3, 'Lixies', 'lixie@msn'),
        User(4, 'Tixies', 'tixie@msn')
    ]


def test_update_email(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    user =repository.find(3)
    user.email = "lixie@msn.co.uk"
    repository.update_email(user)
    result = repository.all()
    print(result)
    assert result == [
        User(1, 'Pixies', 'pixie@msn'),
        User(2, 'Dixies', 'dixie@msn'),
        User(3, 'Lixies', 'lixie@msn.co.uk'),
        User(4, 'Tixies', 'tixie@msn'),
    ]