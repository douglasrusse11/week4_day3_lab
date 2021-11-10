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

if __name__ == '__main__':
    app.run(debug=True)
