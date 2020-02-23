from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_author.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

books_authors = db.Table('books_authors', 
              db.Column('book_id', db.Integer, db.ForeignKey('book.id', ondelete='cascade'), primary_key=True), 
              db.Column('author_id', db.Integer, db.ForeignKey('author.id', ondelete='cascade'), primary_key=True))

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45))
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    author_of_book = db.relationship('Author', secondary=books_authors)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    notes = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    books_from_this_author = db.relationship('Book', secondary=books_authors)
    
@app.route("/", methods = ['GET', 'POST'])
def book():
    all_books = Book.query.all()
    return render_template("books.html", all_books=all_books)

@app.route("/add_book", methods=['POST'])
def add_book():
    new_book = Book(title=request.form['title'], description=request.form['description'])
    db.session.add(new_book)
    db.session.commit()
    return redirect("/")

@app.route("/books/<id>", methods = ['GET', 'POST'])
def book_view(id):
    book_with_id = Book.query.get(id)
    all_authors = Author.query.all()
    return render_template("book_view.html", book_with_id = book_with_id, all_authors=all_authors)

@app.route("/book_to_author", methods=['POST'])
def book_to_author(id):
    existing_author = Author.query.get(request.form['author.id'])
    existing_book = Book.query.get(book['id'])
    existing_author.books_from_this_author.append(existing_book)
    db.session.commit()
    return redirect("/books/<id>")

@app.route("/authors", methods = ['GET', 'POST'])
def author():
    all_authors = Author.query.all()
    return render_template("authors.html", all_authors=all_authors)

@app.route("/add_author", methods = ['POST'])
def add_author():
    new_author = Author(first_name=request.form['fname'], last_name=request.form['lname'], notes=request.form['notes'])
    db.session.add(new_author)
    db.session.commit()
    return redirect("/authors")

@app.route("/authors/<id>")
def author_view(id):
    author_with_id = Author.query.get(id)
    all_books = Book.query.all()


    return render_template("author_view.html", author_with_id = author_with_id, all_books=all_books)

if __name__ == "__main__":
    app.run(debug=True)