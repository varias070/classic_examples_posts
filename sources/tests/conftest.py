import falcon
import psycopg
import pytest
from classic.db_tools import ConnectionPool, Engine
from classic.operations import Operation
from falcon import testing

from posts.resource import (
    AuthorResource,
    GetAuthor,
    CreateAuthor,
)
from posts.mapping import mapping
from posts.settings import TestSetting


settings = TestSetting()

def make_conn():
    return psycopg.connect(
        dbname=settings.TEST_DB_NAME,
        user=settings.TEST_DB_USER,
        password=settings.TEST_DB_PASSWORD,
        host=settings.TEST_DB_HOST,
        port=settings.TEST_DB_PORT
    )


def get_engine(mapping):
    pool = ConnectionPool(make_conn)
    return Engine(
        pool,
        templates_dirs=settings.QUERY_REPO_PATH,
        default_mapping=mapping
    )

@pytest.fixture
def engine():
    return get_engine(mapping)


@pytest.fixture
def get_author(engine):
    return GetAuthor(engine)


@pytest.fixture
def create_author(engine):
    return CreateAuthor(engine)


@pytest.fixture
def author_resource(get_author, create_author, engine):
    operation = Operation(engine)
    resource = AuthorResource(
        operation_=operation,
        get_author=get_author,
        create_author=create_author
    )
    return resource


@pytest.fixture
def get_app(author_resource):
    app = falcon.App()
    app.add_route("/author", author_resource)
    # app.add_route("/channel", channel_resource)
    # app.add_route("/post", post_resource)
    return app


@pytest.fixture
def client(get_app):
    return testing.TestClient(get_app)
