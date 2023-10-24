from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Pet Model
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    photo_url = db.Column(db.String(500), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(500), nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)
