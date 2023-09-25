from app import db
from flask_sqlalchemy import SQLAlchemy
from traitlets import validate
from enum import Enum

class HeroPower(db.Model):
   
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)
    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')
    strength = db.Column(db.String(200), nullable=False, validate=validate.OneOf(['Strong', 'Weak', 'Average']))

# We define an Enum class StrengthEnum to represent the possible values for the strength field. This ensures that strength can only have one of the predefined values: 'Strong', 'Weak', or 'Average'.
class StrengthEnum(Enum):
    STRONG = 'Strong'
    WEAK = 'Weak'
    AVERAGE = 'Average'
        