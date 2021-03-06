from . import db


class Feedback(db.Model):
    __tablename__ = "Feedback"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(50), nullable=False)
    category = db.Column(db.VARCHAR(50), nullable=False)
    ivertinimas = db.Column(db.VARCHAR(50), nullable=False)
    kodas = db.Column(db.Integer, nullable=False)
    description = db.Column(db.VARCHAR(200), nullable=False)
    views = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
