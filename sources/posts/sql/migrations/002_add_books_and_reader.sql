CREATE TABLE book (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author INTEGER REFERENCES author(id) ON DELETE SET NULL,
    price NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    quantity INTEGER
)

CREATE TABLE reader (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone VARCHAR(30)
)

CREATE TABLE rental (
    id SERIAL PRIMARY KEY,
    cost NUMERIC(10,2) NOT NULL CHECK (cost >= 0),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    reader INTEGER REFERENCES reader(id) ON DELETE SET NULL
)

CREATE TABLE item (
    id SERIAL PRIMARY KEY,
    book INTEGER REFERENCES book(id) ON DELETE SET NULL
    quantity INTEGER,
    price NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    rental INTEGER REFERENCES rental(id) ON DELETE SET NULL
);
