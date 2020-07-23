from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# API works with resources and every resource must be a class (Student is a resource that can
# only be accessed with a GET method)
class Student(Resource):
    def get(self, name):
        return {'student': name}


api.add_resource(Student, '/student/<string:name>')     # adding route/endpoint

app.run(port=5000)
