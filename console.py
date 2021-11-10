from respositories import author_repository
from respositories import book_repository

authors = author_repository.select_all()
print(authors)

books = book_repository.select_all()
print(books)

book_repository.delete(1)