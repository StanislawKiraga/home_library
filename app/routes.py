from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from app.forms import BookForm
from app.models import Book, Author, Borrowed


@app.route('/books/', methods=['GET', 'POST']) 
def home():
    form = BookForm()
    books_list = Book.query.all()
    if request.method == 'POST':     
        if form.validate_on_submit():
            author_name = form.author.data
            author = Author.query.filter_by(name=author_name).first()
            if author is None:
                author = Author(name=author_name)
                db.session.add(author)     
            book = Book(title=form.title.data, author=author, read=form.read.data, borrowed=form.borrowed.data)       
            db.session.add(book)
            db.session.commit()
            return redirect(url_for('home'))
 
    return render_template('books.html', form=form, books_list=books_list)

@app.route('/books/<int:book_id>', methods=['GET', 'POST'])
def update(book_id):
    book = Book.query.get_or_404(book_id)
    form = BookForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            author_name = form.author.data
            book
            author = Author.query.filter_by(name=author_name).first()
            if author is None:
                author = Author(name=author_name)
                db.session.add(author)
            book.title = form.title.data
            book.read = form.read.data
            book.borrowed = form.borrowed.data
            db.session.commit()
            return redirect(url_for('home'))
        
    form.title.data = book.title
    form.author.data = book.author.name if book.author else ''
    form.read.data = book.read
    form.borrowed.data = book.borrowed

    return render_template('book.html', form=form, book=book)

@app.route('/delete_book/<int:book_id>', methods=['GET', 'POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('book.html', book=book)

