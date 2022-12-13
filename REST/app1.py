# Build an API that performs CRUD operations on movie data
# Movies | Title, Rating, Genre

# Import Libraries from Flask Framework
from flask import Flask, jsonify

# Create your flask app
app = Flask(__name__)

# Every flask function HAVE to return JSON or HTML
movies =    [   {'name':'Harry Potter', 'rating': '5',  'genre': 'adventure'},
                {'name':'Star Wars', 'rating': '7',     'genre': 'action'},
                {'name':'Saw', 'rating': '8',           'genre': 'horror'},
                {'name':'Adams Family', 'rating': '3',  'genre': 'horror'},
                {'name':'Attack on Titan', 'rating': '2', 'genre': 'action'},
                {'name':'Lion King', 'rating': '4',     'genre': 'action'},
                {'name':'Saw', 'rating': '6',           'genre': 'adventure'},
                {'name':'Sailor Moon', 'rating': '8',   'genre': 'horror'},
                {'name':'Avatar', 'rating': '7',        'genre': 'action'},
                {'name':'Titatnic', 'rating': '2',      'genre': 'adventure'}
            ]

# Create a function that finds the average rating
@app.route('/rating', methods=['GET'])
def avgRating():
    # avg = total/num
    total = 0
    for i in range(0,len(movies)):
        rating = movies[i]["rating"]
        total += int(rating)

    average = total/len(movies)
    return jsonify({'data':average})


# Create a function that finds the most popular genre in the database
# Frequency Pattern - Uses a dictionary to keep track of counts
@app.route('/popularGenre', methods=['GET'])
def popularGenre():
    # List of Genres: Adventure, Horror, Action
    # Counter += 1 | Adventure
    # AdventureCount greater than Horror 
    genres = {}
    for i in range(0, len(movies)):
        genre = movies[i]['genre']
        if genre in genres:
            genres[genre] += 1
        else:
            genres[genre] = 1

    print(genres)       #{'adventure': 3, 'action': 4, 'horror': 3}
    max = 0
    category = ''
    for genre in genres:
        count = genres[genre]
        if count > max:
            max = count
            category = genre

    return jsonify({'data':category})

# Create a function that returns a list of the movies available
@app.route('/movies', methods=['GET'])
def getMovies():
    titles = []
    for i in range(0, len(movies)):
        titles.append(movies[i]['name'])
    
    return jsonify({'data':titles})


# Letter Counter | faraz | kamran | rakin
def letterCounter(str):
    counter = {}
    for letter in str:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    return counter

print(letterCounter('Faraz'))
print(letterCounter('Khuzaima'))

# Starts the flask server
app.run(debug=True)