from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {1: {'age' : 40, 'tumor' : 'malignant'},
         2: {'age': 70, 'tumor': 'benign'}}

class Hello(Resource):
    def get(self, id):
        return names[id]

    def post(self):
        return {'data': 'Posted'}

api.add_resource(Hello, '/hello/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)