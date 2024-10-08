# import sqlite3

# db = sqlite3.connect("books.collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
try:
    with app.app_context():
        # Create table if not exists
        # db.create_all()
        # Add record
        new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
        db.session.add(new_book)
        db.session.commit()
except Exception as err:
    print(err)   
finally:
    with app.app_context():
        books = Book.query.all()
        print(books)

if __name__ == "__main__":
    app.run(debug=True)