from flask_sqlalchemy import SQLAlchemy

def DB(app):
    return SQLAlchemy(app)
 