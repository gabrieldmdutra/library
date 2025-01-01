from app import db

class Users(db.Model):
    username = db.Column(db.String(10), primary_key=True)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f'<Name {self.name}>'

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(40), primary_key=True)
    author = db.Column(db.String(40), nullable=False)
    is_read = db.Column(db.Boolean, nullable=False)
    comments = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Title {self.title}>'
