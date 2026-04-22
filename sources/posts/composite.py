import falcon
import psycopg

from classic.operations import Operation
from classic.falcon_integration import register_all
from classic.db_tools import Engine, ConnectionPool

from .mapping import mapping
from .settings import Setting
from .use_case import (
    GetAuthor,
    CreateAuthor,
    GetChannel,
    CreateChannel,
    GetPost
)
from .resource import (
    AuthorResource,
    ChannelResource,
    PostResource
)


settings = Setting()

def make_conn():
    return psycopg.connect(
        dbname=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT
    )


def get_engine(mapping):
    pool = ConnectionPool(make_conn)
    return Engine(
        pool,
        templates_dirs=settings.QUERY_REPO_PATH,
        default_mapping=mapping
    )


engine = get_engine(mapping=mapping)
operation = Operation(engine)


author_resource = AuthorResource(
    operation_=operation,
    get_author=GetAuthor(engine=engine),
    create_author=CreateAuthor(engine=engine)
)
channel_resource = ChannelResource(
    operation_=operation,
    get_channel=GetChannel,
    create_channel=CreateChannel
)
post_resource = PostResource(
    operation_=operation,
    get_post=GetPost
)

app = falcon.App()
app.add_route("/author", author_resource)
app.add_route("/channel", channel_resource)
app.add_route("/post", post_resource)

register_all(app)

if __name__ == "__main__":
    import waitress
    waitress.serve(app, host="127.0.0.1", port="8000")
