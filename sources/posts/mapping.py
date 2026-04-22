from classic.db_tools import Entity

from posts.model import Post, Author, Channel


mapping = dict(
    post=Entity(Post, 'id'),
    author=Entity(Author, 'id'),
    channel=Entity(Channel, 'id')
)
