import sqlite3
from db import db

# The UserModel is iin fact an API. It is not a REST API, but it is an API with two endpoints: find_by_username, and find_by_id.
# These methods are an interface for other parts of our program to interact with the User "thing".


class UserModel(db.Model):
    # Tell SQLAlchemy the table name where these models will be stored
    __tablename__ = 'users'

    # Tell SQLAlchemy what columns the table should contain
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod    # Allows you too change 'Self' & 'User to 'cls'
    # def find_by_username(self, username):
    def find_by_username(cls, username):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM users WHERE username=?"
        # result = cursor.execute(query, (username,))
        # row = result.fetchone()
        # if row:
        #     # user = User(row[0], row[1], row[2])
        #     # user = cls(row[0], row[1], row[2])
        #     user = cls(*row)
        # else:
        #     user = None

        # connection.close()
        # return user

        # SELECT * FROM users WHERE username=username LIMIT 1
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM users WHERE id=?"
        # result = cursor.execute(query, (_id,))
        # row = result.fetchone()
        # if row:
        #     # user = User(row[0], row[1], row[2])
        #     # user = cls(row[0], row[1], row[2])
        #     user = cls(*row)
        # else:
        #     user = None

        # connection.close()
        # return user
        return cls.query.filter_by(id=_id).first()
