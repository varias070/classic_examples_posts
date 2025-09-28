import falcon
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from classic.operations import Operation
from classic.falcon_integration import register_all

from . import database, resource
from .settings import Setting


settings = Setting()
engine = create_engine(settings.DB_URL)
session_builder = sessionmaker(engine)
session = scoped_session(session_builder)
operation = Operation(
    before_start=session.begin,
    after_complete=session.commit,
    on_cancel=session.rollback,
    on_finish=session.close,
)

author_repo = database.AuthorRepo(
    session=session,
    operation_=operation,
)
channel_repo = database.ChannelRepo(
    session=session,
    operation_=operation,
)
post_repo = database.PostRepo(
    session=session,
    operation_=operation,
)

author_resource = resource.AuthorResource(
    author_repo=author_repo,
    operation_=operation,
)
channel_resource = resource.ChannelResource(
    channel_repo=channel_repo,
    operation_=operation,
)
post_resource = resource.PostResource(
    post_repo=post_repo,
    operation_=operation,
)

app = falcon.App()
app.add_route("/author", author_resource)
app.add_route("/channel", channel_resource)
app.add_route("/post", post_resource)

register_all(app)

if __name__ == "__main__":
    import waitress
    waitress.serve(app, host="127.0.0.1", port="8000")
