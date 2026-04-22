INSERT INTO author (name, phone)
VALUES (%(name)s, %(phone)s)
RETURNING id;