from classic.db_tools import Engine, ConnectionPool
import psycopg

from sources.posts.settings import Setting

settings = Setting()

def make_conn():
    return psycopg.connect(
        dbname=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT
    )

pool = ConnectionPool(make_conn)
engine = Engine(pool, settings.QUERY_REPO_PATH)

with engine:
    engine.query_from('001_init.sql').execute()
    engine.query_from('create_author.sql').executemany([
        {"name": "first", "phone": "79002003040"},
        {"name": "second", "phone": "79001002030"},
    ])
    engine.query_from('create_channel.sql').executemany([
        {"author_id": 1, "title": "first", "login_data": "dvaeaef"},
        {"author_id": 2, "title": "second", "login_data": "feafafs"}
    ])
    engine.query_from('create_post.sql').executemany([
        {"channel_id": 1, "title": "first post", "text": "hello"},
        {"channel_id": 2, "title": "second post", "text": "good by"},
    ])