from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'Benny'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # new endpoint: "/auth"

items = []


# API works with resources and every resource must be a class (Item is a resource that can
# only be accessed with a GET method)
class Item(Resource):
    @jwt_required()
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        # next() - returns first item matched by filter function
        # return {'item': None}, 404
        # -or-
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        # data = request.get_json(force=True)   - force=True will format content-Type header even if it is not set to application/json
        # data = request.get_json(silent=True)  - silent=True will not send the 'no-header' error
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item,

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')     # adding route/endpoint
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
