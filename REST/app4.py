#  Import Flask
from flask import Flask, request        # Request is flask's module to view the request details
from flask import render_template       # Flask's library to deliver HTML
from flask import jsonify               # Flask's library to deliver JSON

# Create a new instance of flask
app = Flask(__name__)

# A flask function HAS to return JSON or HTML
# A flask function can't be called by its name. It gets run by its route. Ex. /contact
# A flask function can't have arugments passed in. It gets any data from the request
@app.route('/myName', methods=['GET'])
def getName():
    return jsonify({'name':'Faraz'})

# Make this function a route
# Create a function that calculates area of a triangle
# Accepts the base and height as arugments
@app.route('/triangleArea', methods=['GET'])
def triangleArea():
    b = request.args.get('b')
    h = request.args.get('h')
    a=0.5*int(b)*int(h)
    return jsonify({'area':a})

# Make this function a route
# Create a 4 item data model where every movie has a title, year, and date
# Create a function that returns a list of movie titles
@app.route('/movies', methods=['GET'])
def movieList():
    movies = [{"title": "Lion King"
                "year": "2000"
                "date": "02-04-2001"},

                {"title": "Home Alone"
                "year": "2003"
                "date": "04-04-2003"},

                {"title": "Bat Man
                "year": "2010"
                "date": "12-04-2010"}]

    titles = []
    for i in range(0,len(movies)):
        movie = movies[i]["title"]
        titles.append(movie)

    return jsonify({"data":titles})

# Arguments made to GET requests have a question mark followed by arugments
# Ex. /sum?x=5&y=12&name='bob'
@app.route('/sum', methods=['GET'])
def sum():
    x = request.args.get('x')
    y = request.args.get('y')
    name = request.args.get('name')
    print(name)
    total = int(x) + int(y)

    return jsonify({'data':total})


# Port 5000 is flask's native port
# Run the flask server which servers your endpoints
# 127.0.0.1 or localhost
app.run(port=4999, debug=True)


"""
class Flask():
    def __init__():
        # Setup
    
    def route():
        # Creates a flask route

    def run():
        # Starts the flask server

class Car():
    def __init__(self, year):
        # Properties are set here
        self.year = year
        self.name = ''

car1 = Car(1992)
car2 = Car(1958)

"""
"""
import json 

file = open('imdb_movie.json')
data = json.load(file) 
"""