from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from app.forms import BookForm
from app.models import Book, Author, Borrowed

@app.route('/books/', methods=['GET', 'POST'])
def home():
    form = BookForm()
    book = Book()
    error = ''
    if request.method == 'POST':
        if form.validate_on_submit():
            

