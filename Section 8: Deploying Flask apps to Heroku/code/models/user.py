import sqlite3
from db import db


class UserModel(db.Model):
    # Tell SQLAlchemy the table name where these models will be stored
    __tablename__ = 'users'

    # Tell SQLAlchemy what columns the table should contain
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod    # Allows you too change 'Self' & 'User to 'cls'
    # def find_by_username(self, username):
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
