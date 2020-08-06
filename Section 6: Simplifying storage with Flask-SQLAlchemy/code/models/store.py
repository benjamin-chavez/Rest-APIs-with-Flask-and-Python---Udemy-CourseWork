from db import db


class StoreModel(db.Model):
    # Specify SLQAlchemy table name
    __tablename__ = 'stores'

    # Specify SLQAlchemy columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # Back reference: allows a store to look at items and find the related items
    # items is a list of item of item models
    # lazy='dynamic' -> this stops self.items from being a list of items and instead
    # is a query builder that has the ability to look into the items table. In adding
    # this you must add .all() to self in the json method in order to build the list.
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    # Json method returns a json representation of the Item Model
    def json(self):
        return{'name': self.name, 'items': [item.json() for item in self.items.all()]}

    # Find_by_name is still a class method because it returns an
    # object of type StoreModel as apposed to a dictionary
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
