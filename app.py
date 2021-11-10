from flask import Flask, render_template, redirect
from respositories import author_repository, book_repository
app = Flask(__name__)

@app.route('/')
def home():
    books = book_repository.select_all()
    return render_template('index.html', books=books)

@app.route('/<id>', methods = ['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
