from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    read = db.Column(db.Boolean, default=False)
    borrowed = db.Column(db.Boolean, default=False)

    def __str__(self):
        return f'<Book {self.id}'
    
books_authors = db.Table('books',
                         db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
                         db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
 )


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref=db.backref('author'), lazy=True)

    def __str__(self):
        return f'{self.name}'
    
class Borrowed(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    def __str__(self):
        return f'<Available: {self.available}>'

    
