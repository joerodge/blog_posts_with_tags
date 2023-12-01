from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/blog_posts_tags.sql")

post_repo = PostRepository(connection)
posts = post_repo.find_by_tag('coding')
print('Here are all the posts with tag "coding":')
for post in posts:
    print(f"  * {post.post_id} - {post.title}")

tags = post_repo.find_by_post(3)
print('Here are all the tags for post 3:')
for tag in tags:
    print(f"  * {tag.tag_id} - {tag.name}")
