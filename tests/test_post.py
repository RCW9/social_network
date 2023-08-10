from lib.post import Post

"""
post constructs with an id, name and genre
"""
def test_post_constructs():
    post = Post(1, "Test title", "Test content", 25, 2)
    assert post.id == 1
    assert post.title == "Test title"
    assert post.content == "Test content"
    assert post.views == 25
    assert post.user_id == 2

"""
We can format posts to strings nicely
"""
def test_post_formats_nicely():
    post = Post(1, "Test title", "Test content", 25, 2)
    assert str(post) == "post(1, Test title, Test content, 25, 2)"


"""
We can compare two identical posts
And have them be equal
"""
def test_posts_are_equal():
    post1 = Post(1, "Test title", "Test content", 25, 2)
    post2 = Post(1, "Test title", "Test content", 25, 2)
    assert post1 == post2