from . import db


class User(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(50), nullable=False, unique=True)
    password = db.Column(db.VARCHAR(50), nullable=False)
    email = db.Column(db.VARCHAR(50), nullable=False, unique=True)
    feedback = db.relationship('Feedback', backref="user", lazy=True)
    