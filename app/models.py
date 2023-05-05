from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    borrowed = db.relationship('Borrowed', backref='book', lazy='select')

    def __str__(self):
        return f'<Book {self.id}'
    

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship('Book', backref='author', lazy='select')

    def __str__(self):
        return f'<Author {self.id}>'
    
class Borrowed(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    available = db.Column(db.String)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f'<Available: {self.available}>'