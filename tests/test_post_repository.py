from lib.post_repository import PostRepository
from lib.posts import Post, Tag

def test_find_by_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    post_repo = PostRepository(db_connection)
    posts = post_repo.find_by_tag('coding')
    # should return post 1, 2, 3, 7
    assert posts == [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(7, 'SQL basics'),
    ]

# This method should accept a post ID, and return an array of related Tag objects.
def test_find_tags_by_post(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    post_repo = PostRepository(db_connection)
    # Post 6 is 'A foodie week in Spain' with tags 2 (travel) & 3 (cooking)
    tags = post_repo.find_by_post(6)
    assert tags == [
        Tag(2, 'travel'),
        Tag(3, 'cooking')
    ]

def test_find_tags_by_post2(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    post_repo = PostRepository(db_connection)
    # Post 6 is 'A foodie week in Spain' with tags 2 (travel) & 3 (cooking)
    tags = post_repo.find_by_post(2)
    assert tags == [
        Tag(1, 'coding'),
        Tag(4, 'education')
    ]