from db.run_sql import run_sql

from models.author import Author
from models.book import Book
from respositories import author_repository

def select_all():
    books = []

    sql = f"SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row["author_id"])
        book = Book(row['title'], author, row['id'])
        books.append(book)
    return books

def select(id):
    book = None

    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        author = author_repository.select(result["author_id"])
        book = Book(result["title"], author, result["id"])
    return book



def delete(id):
    sql = f"DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(book):
    sql = f"INSERT INTO books (title, author_id) VALUES (%(title)s, %(author_id)s) RETURNING *"
    values = {'title': book.title, 'author_id': book.author.id}
    result = run_sql(sql, values)
    id = result[0]["id"]
    book.id = id

def update(book):
    sql = "UPDATE books SET (title, author_id) = (%(title)s, %(author_id)s) WHERE id = %(id)s" 
    values = {'title': book.title, 'author_id': book.author.id, 'id': book.id}
    run_sql(sql, values)