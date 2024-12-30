from flask import Flask
from repository.repository import DB

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = DB(app)

from views import *
from controllers import *

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

