INSERT INTO post (channel_id, title, text)
VALUES (%(channel_id)s, %(title)s, %(text)s)
RETURNING id;