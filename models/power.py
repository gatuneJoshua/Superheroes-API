from app import db
from flask_sqlalchemy import SQLAlchemy

class Power(db.Model) :
   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    heroes = db.relationship('Hero', secondary='hero_power', back_populates='powers')