import json     # Convert a json dataset to a dictionary
import pymongo


def convertToJson():
    file = open("shows.json")
    movies = json.load(file)
    return movies['data']

def connectToDB(tableName):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['netflix']
    collection = db[tableName]
    return collection

def insertToDB():
    movieData = convertToJson()
    collection = connectToDB('movies')

    for i in range(0, len(movieData)):
        collection.insert_one(movieData[i])

if __name__ == "__main__":
    insertToDB()