#!/usr/bin/env python3


from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import  db, Hero

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/', methods=['GET'])
def heroes():
    heroes = []
    for hero in Hero.query.all():
         hero_dict = {
            "name": hero.name,
             "super_name": hero.super_name,
              
        }
    heroes.append(hero_dict)
    
    response = make_response(
        jsonify(heroes),
        200
    )        
    return response

       

  

@app.route('/heroes/<int:id>', methods=['GET'])
def hero(id):
    hero = Hero.query.get(id)
    if hero is None:
        return jsonify({"error": "Not found"}), 404
   # schema = HeroSchema()
    #return jsonify(schema.dump(hero))
 


if __name__ == '__main__':
    app.run(port=5555)
