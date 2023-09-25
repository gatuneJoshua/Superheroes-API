#from app import db
from flask_sqlalchemy import SQLAlchemy
from models.config import db
class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    super_name = db.Column(db.String(200), nullable=False)
    powers = db.relationship('HeroPower',backref = db.backref('heroes'))