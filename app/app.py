from flask import Flask
from flask_restx import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world!"}


@api.route('/test')
class Tester(Resource):
    def get(self):
        connection_string = "mongodb://user1:1528@52.78.23.245/train"
        client = MongoClient(connection_string)

        db_handle = client['train']
        collection_name = db_handle['train']

        train1 = {
            "medicine_id": "RR000123456",
            "common_name": "Paracetamol",
            "scientific_name": "",
            "available": "Y",
            "category": "fever"
        }
        train2 = {
            "medicine_id": "RR000123456",
            "common_name": "Paracetamol",
            "scientific_name": "",
            "available": "Y",
            "category": "fever"
        }

        collection_name.insert_many([train1, train2])
        count = collection_name.count()

        names = ''
        med_details = collection_name.find({})
        for r in med_details:
            names = r["common_name"]
        return {"data": "Hello, world. You're at the polls index. count : " + str(count) + ", names : " + names}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9001)