# IMDB

"""
User
    name
    email
    password
    Review

Movie
    name
    releaseDate
    genre
    overallRating
    Actors

Review
    rating
    movie
    description

Actor
   name
   bio
"""

# DATA MODELS

 # OOO - Classes

 # Class - Data Structures -> Contains Data & Functions


class Actor():

    def __init__(self):
        self.name = ""
        self.bio = ""

    def getActorName(self):
        return self.name
    def setActorName(self, name): 
        self.name = name

    def getActorBio(self): 
        return self.bio
    def setActorBio(self, bio):
        self.bio = bio

    def getSummary(self):
        return {'name':self.name, 'bio':self.bio}


actor1 = Actor()
actor1.setActorName('Brad Pitt')
actor1.setActorBio('The famed star is....')
print(actor1.getSummary())

actor2 = Actor()
print(actor2.getSummary())


class Movie():
    def __init__(self, name, releaseDate, genre):
        self.name = name
        self.release = releaseDate
        self.genre = genre
        self.rating = 0
        self.actors = []

    def getRating(self):
        return self.rating

    def setRating(self, rating):
        if isinstance(rating, int):
            self.rating = rating 
        else:
            print('YOU FOO!')

    def getActors(self):
        return self.actors

    def setActor(self, actor):
        self.actors.append(actor) 


movie = Movie("Aladdin", "1992", 'Cartoon')
print(movie)
movie.setActor('Brad Putt')
movie.setActor('Joe Shmoe')
movie.setActor('Botswanne Kareem')
movie.setRating([4])
movie.setRating(4)

print(movie.getRating())
print(movie.getActors())

movie2 = Movie("Sleeping Butty", "1942", 'Live Action')
print(movie2)















