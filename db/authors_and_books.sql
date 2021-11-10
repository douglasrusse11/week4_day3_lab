DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_id INT REFERENCES authors(id) ON DELETE CASCADE
);

INSERT INTO authors (name) VALUES ('JRR Tolkien');
INSERT INTO books (title, author_id) VALUES ('The Hobbit', 1);