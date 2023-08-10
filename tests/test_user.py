from lib.user import User

"""
User constructs with an id, name and genre
"""
def test_artist_constructs():
    user = User(1, "Test username", "Test email")
    assert user.id == 1
    assert user.username == "Test username"
    assert user.email == "Test email"

"""
We can format user to strings nicely
"""
def test_user_formats_nicely():
    user = User(1, "Test username", "Test email")
    assert str(user) == "user(1, Test username, Test email)"


"""
We can compare two identical user
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "Test username", "Test email")
    user2 = User(1, "Test username", "Test email")
    assert user1 == user2