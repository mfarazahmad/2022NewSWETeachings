# CRUDnet

# Data Model - Topic

import json
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Wrapper function
@app.route('/test', methods = ['GET'])
def test():
    print(request.headers)
    return jsonify({'show':5})

# Views - A route that delivers HTML

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

    # How does your frontend connect to backend?

# REST APIs - A route that delivers JSON

# POST Examples | How to get data from the request body
@app.route('/saveMovie', methods=['POST'])
def saveMovie():
    # Colect the data from the frontend
    data = request.json
    print(data)

    # Save the Data
    # Connect to DB
    # db = Mongo('127.0.0.1:27017')
    # db.save(data)

    return jsonify({'msg': 'Success!'})

# Response to display movies
@app.route('/getMovies', methods=['GET'])
def getMovies():
    # Connect to DB
    # db = Mongo('127.0.0.1:27017')
    # movies = db.get('movies')
    file = open('shows.json')       # Open a file in python
    movies = json.load(file)        # Converts a json file to dict
    movies = movies['data']

    return jsonify({'data':movies})

#----- Backend Features ------

# As a User I would like for there to be a way to Edit My Movie Details

# As a User I would like for there a way to search for my Favorite Movie

# Error Handling

# What is your successful scenario?
    # Network Connection -> JS Ajax to Python Flask
    # Is the data good. Validation

# When isn't your successful scenario?
    # What do you show to the user when it doesnt work out?
    # What do you print or log to show the Engineer why?

# Backlog - A list of tasks we will do in the future
    # Add to Favorites
    # Playlist Movies


app.run(debug=True)




# Libraries allow you to do different things |
import requests # Requests to do GET, POST, PUT, DELETE
resp = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
print(resp.json())