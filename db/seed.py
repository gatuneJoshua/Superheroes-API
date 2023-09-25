from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Power, Hero, HeroPower
from random import randint, choice

# Initialize SQLAlchemy engine and session
engine = create_engine('sqlite:///your_database_name.db')
Session = sessionmaker(bind=engine)
session = Session()

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
    session.add(power)

session.commit()
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
    session.add(hero)

session.commit()
print("🦸‍♀️ Seeding heroes complete!")

# Adding powers to heroes
print("🦸‍♀️ Adding powers to heroes...")
strengths = ["Strong", "Weak", "Average"]

for hero in session.query(Hero).all():
    for _ in range(randint(1, 3)):
        power = session.query(Power).order_by(func.random()).first()  # Get a random power
        hero_power = HeroPower(hero_id=hero.id, power_id=power.id, strength=choice(strengths))
        session.add(hero_power)

session.commit()
print("🦸‍♀️ Done seeding!")
