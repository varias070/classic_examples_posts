CREATE TABLE author (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone VARCHAR(30)
);


CREATE TABLE channel (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    login_data TEXT,
    author_id INTEGER REFERENCES author(id) ON DELETE SET NULL
);


CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    text TEXT,
    channel_id INTEGER REFERENCES channel(id) ON DELETE SET NULL
);
