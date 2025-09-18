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
author_repo = database.AuthorRepo(session=session)
operation = Operation(
    before_start=session.begin,
    after_complete=session.commit,
    on_cancel=session.rollback,
    on_finish=session.close,
)

author_resource = resource.AuthorResource(
    author_repo=author_repo,
    operation_=operation,
)
app = falcon.App()
app.add_route("/author", author_resource)
register_all(app)

if __name__ == "__main__":
    import waitress
    waitress.serve(app, host="127.0.0.1", port="8000")
