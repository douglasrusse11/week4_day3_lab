from db.run_sql import run_sql

from models.author import Author
from models.book import Book

def select_all():
    authors = []

    sql = f"SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['name'], row['id'])
        authors.append(author)
    return authors

def select(id):
    sql = f"SELECT * FROM authors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['name'], result['id'] )
    return author

def delete(id):
    sql = f"DELETE FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def books(author):
    books = []
    sql = f"SELECT * FROM books WHERE author_id = %s"
    values = [author.id]
    results = run_sql(sql, values)
    for row in results:
        book = Book(row["title"], author, row["id"])
        books.append(book)
    return books