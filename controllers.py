from app import app
from app import db

from flask import redirect
from flask import url_for
from flask import request
from flask import flash

from models import Users
from models import Books


@app.route("/auth", methods=['POST'])
def auth():
    username = request.form['username']
    password = request.form['password']
    user = Users.query.filter_by(username=username).first()

    if user and password == user.password:
        return redirect(url_for('index'))

    return redirect('login')

@app.route("/create", methods=['POST'])
def create():
    title = request.form['title']
    author = request.form['author']

    try:
        request.form['read']
        is_read = True
    except KeyError:
        is_read = False

    book = Books.query.filter_by(title=title).first()
    if book:
        flash('The has already been registered!')
        return redirect('index')

    new_book = Books(
        title=title,
        author=author,
        is_read=is_read
    )

    db.session.add(new_book)
    db.session.commit()

    return redirect(url_for('index'))

@app.route("/update", methods=['POST'])
def update():
    book = Books.query.filter_by(id=request.form['id']).first()

    book.title = request.form['title']
    book.author = request.form['author']

    try:
        request.form['read']
        book.is_read = True
    except KeyError:
        book.is_read = False

    db.session.add(book)
    db.session.commit()

    return redirect(url_for('index'))

@app.route("/delete/<int:id>")
def delete(id):
    Books.query.filter_by(id=id).delete()
    db.session.commit()

    flash(f'The book has been deleted!')
    return redirect(url_for('index'))

def read_book(id):
    return Books.query.filter_by(id=id).first()
