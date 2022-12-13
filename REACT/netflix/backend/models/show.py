# Data Model: Title, Seasons, Genres, Cast, Feelings,  CensoryRating, UserRating, Year, Description

# Rakin - Creating a Data Structure aka a class that holds these

class Show():
    def __init__(self, title, seasons, censorySetting, year):
        self.title = title
        self.seasons = seasons 
        self.genres = []
        self.cast = [] 
        self.feelings = ''
        self.censorySetting = censorySetting
        self.userRating = 0
        self.year = year
        self.description = ''

    def getTitle(self):
        return self.title
    def setTitle(self, title):
        self.title = title

    def getGenres(self):
        return self.genres
    def addGenre(self, genre):
        self.genres.append(genre)

    def getCast(self):
        return self.cast
    def addCast(self, name):
        self.cast.append(name) 

    def getFeelings(self):
        return self.feelings
    def setFeelings(self, feeling):
        self.feelings += ' ' + feeling

    def getUserRating(self):
        return self.userRating
    def setTitle(self, userRating):
        self.userRating = userRating

    def getDescription(self):
        return self.description
    def setDescription(self, desc):
        self.description = desc



show1 = Show("Lion King", "4", "R", 1991)
show1.setTitle('Jurassic Park')