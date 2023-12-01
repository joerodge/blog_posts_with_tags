from lib.posts import Post, Tag

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_by_tag(self, tag):
        rows = self._connection.execute(
            "SELECT posts.id, posts.title " \
            "FROM tags " \
            "JOIN posts_tags ON posts_tags.tag_id = tags.id " \
            "JOIN posts ON posts_tags.post_id = posts.id " \
            "WHERE tags.name = %s", [tag]
        )
        posts = []
        for row in rows:
            posts.append(Post(row['id'], row['title']))
        return posts
    
    def find_by_post(self, post_id):
        rows = self._connection.execute(
            "SELECT tags.id, tags.name " \
            "FROM posts " \
            "JOIN posts_tags ON posts_tags.post_id = posts.id " \
            "JOIN tags ON posts_tags.tag_id = tags.id " \
            "WHERE posts.id = %s", [post_id]
        )
        tags = []
        for row in rows:
            tags.append(Tag(row['id'], row['name']))
        return tags