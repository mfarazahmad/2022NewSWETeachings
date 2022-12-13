from flask import Blueprint, Flask, jsonify, request
from flask_cors import cross_origin
import json, os, requests, pymongo

from scripts.InsertJson import connectToDB
from scripts.GeneratePicture import generatePicture

movieBlueprint = Blueprint('movie', __name__)

@movieBlueprint.route('/movie', methods=['GET'])
@cross_origin()
def getMovies():
    try:
        table = connectToDB('movies')
        data = table.find()
        
        movies = []
        for movie in data:
            del movie['_id']
            #movie['img'] = ''
            movie['img'] = generatePicture(movie['title'])
            movies.append(movie)

        resp = {'msg':'success', 'error': '', 'data':movies}
    except Exception as e:
        print(str(e))
        resp = {'msg':'fail', 'error': str(e), 'data': ''}

    return jsonify(resp)

@movieBlueprint.route('/movie/new', methods=['POST'])
@cross_origin()
def saveMovie():
    try:
        data = request.json
        print(data)
        
        table = connectToDB('movies')
        table.insert_one(data)

        resp = {'msg': 'success', 'error': ''}
    except Exception as e:
        print(str(e))
        resp = {'msg': 'fail', 'error': str(e)}

    return jsonify(resp)

@movieBlueprint.route('/search', methods=['GET'])
@cross_origin()
def findMovie():
    try:
        # Get Search Term from Frontend
        searchTerm = request.args.get('term')

        # Connect to DB to get all the movies
        table = connectToDB('movies')
        movies = table.find()

        # Searching the movie data for the search term
        filterData = []
        for movie in movies:
            del movie['_id']
            if searchTerm.lower() in movie['title'].lower():
                movie['img'] = generatePicture(movie['title'])
                filterData.append(movie)

        return jsonify({'msg': 'success', 'error':'', 'data':filterData})
    except Exception as e:
        print(str(e))
        return jsonify({'msg': 'fail', 'error':str(e), 'data':''})
