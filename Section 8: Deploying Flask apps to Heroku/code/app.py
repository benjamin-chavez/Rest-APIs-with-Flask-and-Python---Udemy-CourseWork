import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///data.db')
# Specify SQLAlchemy configuration property - turns off Flask SQLAlchemy tracker, and instead uses the SQLAlchemy main library tracker
app.config['SQLALCHEMY_TRACK_MODIFACTIONS'] = False
app.secret_key = 'Benny'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # new endpoint: "/auth"

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')     # adding route/endpoint
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

# The following if statement ensures that the app will not run
# in the case where we were importing something from the app.py
# file. Instead it will only run the app when we run this file.
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
