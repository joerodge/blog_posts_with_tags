from lib.posts import Post, Tag

def test_post_creation():
    post = Post(1, 'Test Title')
    assert post.post_id == 1
    assert post.title == 'Test Title'
    assert post.tags == []

def test_post_equal():
    post1 = Post(1, 'Test Title')
    post2 = Post(1, 'Test Title')
    assert post1 == post2

def test_post_repr():
    post = Post(1, 'Test Title')
    assert str(post) == 'Post(1, Test Title)'


def test_tag_creation():
    tag = Tag(1, 'funny')
    assert tag.tag_id == 1
    assert tag.name == 'funny'


def test_tag_equal():
    tag1 = Tag(1, 'funny')
    tag2 = Tag(1, 'funny')
    assert tag1 == tag2


def test_tag_repr():
    tag = Tag(1, 'funny')
    assert str(tag) == 'Tag(1, funny)'