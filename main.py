from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"robbie": {"age": 43, "gender": "male"},
        "rita": {"age": 42, "gender": "female"}}

class HelloWorld(Resource):
    def get(self, name): # this is overriding the get method for when someone sends a get request to our app
        return names[name]

api.add_resource(HelloWorld, "/helloworld/<string:name>") # registering the resource to go to this class at this uri


if __name__ == "__main__":
    app.run(debug=True) # remove debug after development