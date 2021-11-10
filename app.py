from flask import Flask, render_template, redirect, request
from respositories import author_repository, book_repository
from models.book import Book
app = Flask(__name__)

@app.route('/')
def home():
    books = book_repository.select_all()
    authors = author_repository.select_all()
    return render_template('index.html', books=books, all_authors=authors)

@app.route('/<id>', methods = ['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/')

@app.route('/', methods=["POST"])
def add_book():
    title = request.form["title"]
    author = author_repository.select(request.form["author"])
    book = Book(title, author)
    book_repository.save(book)
    return redirect('/')

@app.route('/<id>/edit')
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template("edit.html", book=book, all_authors=authors)

@app.route('/<id>/update', methods=['POST'])
def update_book(id):
    title = request.form["title"]
    author = author_repository.select(request.form["author"])
    book = Book(title, author, id)
    book_repository.update(book)
    return redirect('/')

@app.route('/<id>')
def show_book(id):
    book = book_repository.select(id)
    return render_template("show.html", book=book)

@app.route('/books/<id>')
def show_books_by_author(id):
    author = author_repository.select(id)
    books = author_repository.books(author)
    return render_template("index.html", books=books)


if __name__ == '__main__':
    app.run(debug=True)
