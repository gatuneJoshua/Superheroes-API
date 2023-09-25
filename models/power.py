#from app import db
from flask_sqlalchemy import SQLAlchemy
from models.config import db
class Power(db.Model) :
   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    heroes = db.relationship('HeroPower', backref= db.backref('powers'))