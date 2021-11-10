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
INSERT INTO books (title, author_id) VALUES ('Fellowship of the Ring', 1);
INSERT INTO books (title, author_id) VALUES ('The Two Towers', 1);
INSERT INTO books (title, author_id) VALUES ('Return of the King', 1);
INSERT INTO authors (name) VALUES ('Dan Koeppel');
INSERT INTO books (title, author_id) VALUES ('Banana: The Fate of the fruit that changed the world', 2);

