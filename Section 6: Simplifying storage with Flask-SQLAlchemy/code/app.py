from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

# The following chunk of code was updated once we moved items to its own file.
# from flask import Flask, request
# from flask_restful import Resource, Api, reqparse
# from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# Specify SQLAlchemy configuration property - turns off Flask SQLAlchemy tracker, and instead uses the SQLAlchemy main library tracker
app.config['SQLALCHEMY_TRACK_MODIFACTIONS'] = False
app.secret_key = 'Benny'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # new endpoint: "/auth"

# THE FOLLOWING CHUNK OF CODE WAS MOVED TO item.py WHEN WE INITIALIZED THE USE OF THE
# DATABASE
# items = []

# # API works with resources and every resource must be a class (Item is a resource that can
# # only be accessed with a GET method)
# class Item(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('price',
#                         type=float,
#                         required=True,
#                         help="This field cannot be left blank!"
#                         )

#     @jwt_required()
#     def get(self, name):
#         # for item in items:
#         #     if item['name'] == name:
#         #         return item
#         # next() - returns first item matched by filter function
#         # return {'item': None}, 404
#         # -or-
#         item = next(filter(lambda x: x['name'] == name, items), None)
#         return {'item': item}, 200 if item else 404

#     def post(self, name):
#         if next(filter(lambda x: x['name'] == name, items), None) is not None:
#             return {'message': "An item with name '{}' already exists.".format(name)}, 400
#         # data = request.get_json(force=True)   - force=True will format content-Type header even if it is not set to application/json
#         # data = request.get_json(silent=True)  - silent=True will not send the 'no-header' error
#         # data = request.get_json()
#         data = Item.parser.parse_args()

#         item = {'name': name, 'price': data['price']}
#         items.append(item)
#         return item,

#     # @jwt_required()
#     def delete(self, name):
#         global items
#         items = list(filter(lambda x: x['name'] != name, items))
#         return {'message': 'Item deleted'}

#     # @jwt_required()
#     def put(self, name):
#         # data = request.get_json()
#         data = Item.parser.parse_args()

#         item = next(filter(lambda x: x['name'] == name, items), None)
#         if item is None:
#             item = {'name': name, 'price': data['price']}
#             items.append(item)
#         else:
#             item.update(data)
#         return item

# class ItemList(Resource):
#     def get(self):
#         return {'items': items}


api.add_resource(Item, '/item/<string:name>')     # adding route/endpoint
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# The following if statement ensures that the app will not run
# in the case where we were importing something from the app.py
# file. Instead it will only run the app when we run this file.
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
