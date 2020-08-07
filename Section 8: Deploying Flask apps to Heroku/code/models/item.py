from db import db


class ItemModel(db.Model):
    # Specify SLQAlchemy table name
    __tablename__ = 'items'

    # Specify SLQAlchemy columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # Sets store equal to the store that has the same id
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    # Json method returns a json representation of the Item Model
    def json(self):
        return{'name': self.name, 'price': self.price}

    # Find_by_name is still a class method because it returns an
    # object of type ItemModel as apposed to a dictionary
    @classmethod
    def find_by_name(cls, name):
        # SELECT * FROM items WHERE name=name LIMIT 1
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
