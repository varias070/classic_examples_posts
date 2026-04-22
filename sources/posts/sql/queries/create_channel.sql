INSERT INTO channel (title, login_data, author_id)
VALUES (%(title)s, %(login_data)s, %(author_id)s)
RETURNING id;