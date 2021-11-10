from respositories import author_repository
from respositories import book_repository
from models.author import Author
from models.book import Book

authors = author_repository.select_all()
print(authors)

books = book_repository.select_all()
print(books)

book_repository.delete(1)

author = Author("Dan Koeppel", 2)
book = Book("To See Every Bird on Earth: A Father, a Son, and a Lifelong Obsession", author)
book_repository.save(book)