from classic.db_tools import Engine

from posts.model import Author, Post
from posts.validators import (
    AuthorForSearch,
    AuthorForCreate,
    ChannelForSearch,
    ChannelForCreate
)


class GetAuthor:
    engine: Engine

    def __init__(self, engine):
        self.engine = engine

    def run(self, data):
        filter_obj = AuthorForSearch.model_validate(data)
        with self.engine:
            query = self.engine.query_from("select_author.sql.tmpl").map_to(Author)
            return query.one(**filter_obj.__dict__)


class CreateAuthor:
    engine: Engine

    def __init__(self, engine):
        self.engine = engine

    def run(self, data):
        filter_obj = AuthorForCreate.model_validate(data)
        with self.engine:
            query = self.engine.query_from("create_author.sql")
            return query.scalar(**filter_obj.__dict__)


class GetChannel:
    engine: Engine

    def run(self, data):
        filter_obj = ChannelForSearch.model_validate(data)
        with self.engine:
            query = self.engine.query_from("select_channel.sql.tmpl").map_to(Author)
            return query.one(**filter_obj.__dict__)


class CreateChannel:
    engine: Engine

    def run(self, data):
        filter_obj = ChannelForCreate.model_validate(data)
        with self.engine:
            query = self.engine.query_from("create_author.sql")
            return query.scalar(**filter_obj.__dict__)


class GetPost:
    engine: Engine

    def run(self, post_id):
        with self.engine:
            query = self.engine.query_from("select_post.sql").map_to(Post)
            return query.one(post_id)
