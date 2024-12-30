from app import db

class Users(db.Model):
    username = db.Column(db.String(10), primary_key=True)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f'<Name {self.name}>'
