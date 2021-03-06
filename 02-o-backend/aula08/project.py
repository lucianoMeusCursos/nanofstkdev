# -*- coding: utf-8 -*-
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, Menuitem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/menu/')
def menu():
    menuItem = session.query(Menuitem).all()
    output = ''
    for i in menuItem:
        output += 'restaurant_id: ' + str(i.restaurant_id)
        output += '</br>'
        output += i.name
        output += '</br>'
        output += i.price
        output += '</br>'
        output += i.description
        output += '</br>'
        output += '</br>'
    return  output

@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(Menuitem).filter_by(restaurant_id=restaurant.id)
    output = ''
    for i in items:
        output += 'restaurant_id: ' + str(i.restaurant_id)
        output += '</br>'
        output += i.name
        output += '</br>'
        output += i.price
        output += '</br>'
        output += i.description
        output += '</br>'
        output += '</br>'
    return output

# Se ele for importado execute
if __name__ == '__main__': 
    app.debug = True
    # Roda o servidor
    app.run(host='0.0.0.0', port = 5000)