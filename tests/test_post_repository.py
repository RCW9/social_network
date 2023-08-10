from lib.post_repository import PostRepository
from lib.post import Post

"""
When we call PostRepository#all
We get a list of Post objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new UserRepository

    result = repository.all() # Get all Users

    # Assert on the results
    assert result == [
    Post(1,'Title1', 'Content1', 2, 1),
    Post(2,'Title2', 'Content2', 5, 1),
    Post(3,'Title3', 'Content3', 10, 2),
    Post(4,'Title4', 'Content4', 15, 4),
    Post(5,'Title4', 'Content5', 20, 4),
    Post(6,'Title4', 'Content6', 25, 3),
    Post(7,'Title4', 'Content7', 30, 2)
    ]


def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    post = repository.find(3)
    assert post == Post(3,'Title3', 'Content3', 10, 2)


def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    repository.create(Post(None, 'Title8', 'Content8', 14, 2))

    result = repository.all()
    assert result == [
        Post(1,'Title1', 'Content1', 2, 1),
        Post(2,'Title2', 'Content2', 5, 1),
        Post(3,'Title3', 'Content3', 10, 2),
        Post(4,'Title4', 'Content4', 15, 4),
        Post(5,'Title4', 'Content5', 20, 4),
        Post(6,'Title4', 'Content6', 25, 3),
        Post(7,'Title4', 'Content7', 30, 2),
        Post(8, 'Title8', 'Content8', 14, 2)
        ]
        