from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/books")
def list_books():
    return "Listing books..."

@app.route("/book/<id>")
def describe_book(id=None):
    return render_template('book.html', id=id)

@app.route("/book", methods=['POST'])
def create_book():
    return "Creating books..."

