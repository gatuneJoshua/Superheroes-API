import sys
import os
from urllib.response import addinfo
# Adjust the path to the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, heroes, powers
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models.power import Power
from models.hero import Hero
from models.heropower import HeroPower
from random import randint, choice
from models.config import db
# Initialize SQLAlchemy engine and session
engine = create_engine('sqlite:///app.db')
#Session = sessionmaker(bind=engine)
#session = Session()
with app.app_context():
 # Seeding powers
 print("🦸‍♀️ Seeding powers...")
 powers_data = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
]

 for power_info in powers_data:
    power = Power(**power_info)
    db.session.add(power)

 db.session.commit()
 print("🦸‍♀️ Seeding powers complete!")

# Seeding heroes
 print("🦸‍♀️ Seeding heroes...")
 heroes_data = [
    {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
    {"name": "Doreen Green", "super_name": "Squirrel Girl"},
    {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
    {"name": "Janet Van Dyne", "super_name": "The Wasp"},
    {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
    {"name": "Carol Danvers", "super_name": "Captain Marvel"},
    {"name": "Jean Grey", "super_name": "Dark Phoenix"},
    {"name": "Ororo Munroe", "super_name": "Storm"},
    {"name": "Kitty Pryde", "super_name": "Shadowcat"},
    {"name": "Elektra Natchios", "super_name": "Elektra"}
]

 for hero_info in heroes_data:
    hero = Hero(**hero_info)
    db.session.add(hero)

 db.session.commit()
 print("🦸‍♀️ Seeding heroes complete!")

#  addinfo powers to heroes
#  print("🦸‍♀️ Adding powers to heroes...")
#  strengths = ["Strong", "Weak", "Average"]

#  for h in hero:
#     for _ in range(randint(1, 3)):
#         power = db.query(Power).order_by(func.random()).first()  # Get a random power
#         hero_power = HeroPower(hero_id=hero.id, power_id=power.id, strength=choice(strengths))
#         db.session.add(hero_power)

 db.session.commit()
 print("🦸‍♀️ Done seeding!")
