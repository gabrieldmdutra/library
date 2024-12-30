from app import app
from app import db

from flask import redirect
from flask import url_for
from flask import request
from flask import flash

from models.models import Users
from models.models import Books


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
    read = request.form['read']

    is_read = False

    if read == "on":
        is_read = True

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
