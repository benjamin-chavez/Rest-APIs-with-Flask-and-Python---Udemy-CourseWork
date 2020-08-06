from db import db


class ItemModel(db.Model):
    # Specify SLQAlchemy table name
    __tablename__ = 'items'

    # Specify SLQAlchemy columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Json method returns a json representation of the Item Model
    def json(self):
        return{'name': self.name, 'price': self.price}

    # Find_by_name is still a class method because it returns an
    # object of type ItemModel as apposed to a dictionary
    @classmethod
    def find_by_name(cls, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()

        # if row:
        #     # return{'item': {'name': row[0], 'price': row[1]}}

        #     # Return an ItemModel object below
        #     # return cls(row[0], row[1])
        #     # refactored below:
        #     return cls(*row)

        # SELECT * FROM items WHERE name=name LIMIT 1
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO items VALUES (?, ?)"
        # cursor.execute(query, (self.name, self.price))

        # connection.commit()
        # connection.close()
        db.session.add(self)
        db.session.commit()

    # def update(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "UPDATE items SET price=? WHERE name=?"
    #     cursor.execute(query, (self.price, self.name))

    #     connection.commit()
    #     connection.close()

    #     return {'message': 'Item deleted'}
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
