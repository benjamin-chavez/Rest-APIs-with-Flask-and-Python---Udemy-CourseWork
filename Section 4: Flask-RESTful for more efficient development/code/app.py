from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


# API works with resources and every resource must be a class (Item is a resource that can
# only be accessed with a GET method)
class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item,


api.add_resource(Item, '/item/<string:name>')     # adding route/endpoint

app.run(port=5000)
