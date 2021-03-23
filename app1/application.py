from pymongo import MongoClient
from flask import Flask, request


app = Flask(__name__)
db_client = MongoClient('mongo', port=27017)
database = db_client['ApplicationDB']
collection = database['Users']


@app.route('/')
def main():
    return 'main_page'


@app.route('/show_all')
def show_users():
    result = []
    for res in collection.find():
        result.append(str(res))
    return '\n'.join(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9087)
