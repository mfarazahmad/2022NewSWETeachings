

# Create a complete dataset -> We'll store is a file. | .json
# Create a data model object
# Make data model object do certain things


# IMDB Database



"""
MOVIE
    title
    releaseDate
    overallRating
    ACTORS
        names
        dob
        height
        weight
    genre

USER
    name
    email
    REVIEW(s)
        title
        description
        rating   

"""


import json

file = open('imdb_model.json')
database = json.load(file)
print(database)

print(database['movies'][0]["title"])
movies = database['movies']
for i in range(0,len(movies)):
    print(movies[i]["title"])