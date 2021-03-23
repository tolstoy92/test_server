from pymongo import MongoClient
from flask import Flask, request


app = Flask(__name__)

client = MongoClient('mongo', port=27017)
db = client['ApplicationDB']
collection = db['Users']

@app.route('/')
def main_page():
    template = '<h1>Main page to add users to DB </h1>'
    return template


@app.route('/add/', methods=["GET"])
def add_user():
    users_counter = 0
    for user in collection.find():
        users_counter += 1
    new_user_id = users_counter + 1   
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    data_to_add = {
        'user_id': new_user_id,
        'first_name': first_name,
        'last_name': last_name
    }
    collection.insert_one(data_to_add)
    return 'Added'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9086)
