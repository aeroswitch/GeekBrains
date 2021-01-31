from pymongo import MongoClient
from pprint import pprint

client = MongoClient('127.0.0.1', 27017)

db = client['users_1810']
users = db.users
books = db.books

users.insert_one()