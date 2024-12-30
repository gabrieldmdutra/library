from app import app
from flask import request
from flask import render_template
from models.models import Users


@app.route("/auth", methods=['POST'])
def auth():
    username = request.form['username']
    password = request.form['password']
    user = Users.query.filter_by(username=username).first()

    if user and password == user.password:
        return render_template('list.html')

    return render_template('login.html')
