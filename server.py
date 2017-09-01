from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def HelloWorld():
    return "Hello World!"

@app.route('/restaurants/<int:restaurant_id>')
def ListMenuItems(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id)
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    html = ''
    for i in items:
        html += '''<p><h2>%s</h2>%s<br>%s</p>''' % (i.name, i.price, i.description)
    return html

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
