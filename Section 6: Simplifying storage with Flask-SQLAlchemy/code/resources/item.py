# API works with resources and every resource must be a class (Item is a resource that can
# only be accessed with a GET method)
import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            return item.json()
        return{"message": "Item not found"}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()

        # item = {'name': name, 'price': data['price']}
        # item s/b an object, not a dictionary
        item = ItemModel(name, data['price'])

        try:
            # ItemModel.insert(item)
            item.save_to_db()
        except:
            return{"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    # @jwt_required()

    def delete(self, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "DELETE FROM items WHERE name=?"
        # cursor.execute(query, (name,))

        # connection.commit()
        # connection.close()

        # return {'message': 'Item deleted'}
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return{'message': 'Item deleted'}

    # @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        # updated_item = {'name': name, 'price': data['price']}
        # updated_item = ItemModel(name, data['price'])

        if item is None:
            # try:
            #     updated_item.insert()
            #     # ItemModel.insert(updated_item)
            # except:
            #     return {"message": "An error occured inserting the item"}, 500
            item = ItemModel(name, data['price'])
        else:
            #     try:
            #         # ItemModel.update(updated_item)
            #         updated_item.update()
            #     except:
            #         return {"message": "An error occured updating the item"}, 500
            # # return updated_item
            # return updated_item.json()
            item.price = data['price']

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)

        items = []

        for row in result:
            items.append({'name': row[0], 'price': row[1]})

        connection.close()

        return {"items": items}
