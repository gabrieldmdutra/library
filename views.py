from app import app
from flask import render_template
from models.models import Books

@app.route("/")
def index():
    books = Books.query.order_by(Books.id)
    return render_template('list.html', books=books)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/new")
def new():
    return render_template('new.html')
