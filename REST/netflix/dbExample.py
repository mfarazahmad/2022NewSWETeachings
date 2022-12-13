# Libray to control mongodb
import pymongo

server = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = server['netflix']
print(db)

# Collection - Table | Movies
movieTable = db['Movies']

movieTable.insert_one({'name':'Lion King'})
print('DOne')
import json
file = open('shows.json')
data = json.load(file)

movieTable.insert_many(data['data'])