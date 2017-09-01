from flask import Flask, render_template
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants')
def helloWorld():
    return render_template('restaurants.html', restaurants=session.query(Restaurant).all())

@app.route('/restaurants/<int:restaurant_id>')
def listMenuItems(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template('menus.html', restaurant=restaurant, items=items)

@app.route('/restaurants/<int:r_id>/new')
def newMenuItem(r_id):
    return "new menu item"

@app.route('/restaurants/<int:r_id>/<int:m_id>/edit')
def editMenuItem(r_id, m_id):
    return "edit menu item"

@app.route('/restaurants/<int:r_id>/<int:m_id>/delete')
def deleteMenuItem(r_id, m_id):
    return "delete menu item"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
