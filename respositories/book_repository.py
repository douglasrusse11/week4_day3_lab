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

def delete(id):
    sql = f"DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)