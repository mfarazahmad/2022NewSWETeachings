


# Primitive Data Types: Integer, Booleans, Strings, Floats

name = 'Faraz'
age = 12
isValid = True
grade = 59.2

# Data Structure: Arrays, Dictionaries, Set, Tuples,Classes

names = ['faraz', 'kamran', 'ali']                      # Arrays - Good for list type of data
print(names[1])                                         # Access a List item by its Index
names[1] = 'Ali'                                        # Update a list item by its Index
names.append('Hamza')                                   # Adds a list item to the end of the list
names.pop()                                             # Deletes a list item at the end of the list

# Getting each item in list
for i in range(0, len(names)):
    print(names[i])

student = {'age': 15, 'name': 'joe', 'weight': 572}     # Dictionaries - Good for descriptive data
print(student['age'])                                   # Access a dictionary by its Key
student['age'] = 39                                     # Updating a dictionary value by its Key
student['grade'] = 100                                  # Creating a new key in a dictionary
del student['weight']                                   # Delete a dictiory item by its key

# Getting each key
for item in student:
    print(student[item])

# Loops
for i in range(0, len(names), 2):           # i is a variable that represents the iteration or the counter value | range(start,end,step)
    pass

for item in student:                        # item is a variable that represents the value in a list or a key in a dictionary
    pass

#--------------------------------------------------------------------------------------------------------------------------------------
# Tool: Functions - A piece of code that does something | Use it for a repeatable task or something that can be consolidated
def getName():              # Making a function
    return 'faraz'          # Sends the data inside the scope of the function to the outside scope

getName()                   # You call a function by its name to use it

# Encapsulation - Hiding the details of particular function or class so it can be used without any privacy concerns
# Scope - Python If Statements, For Loops, Classes -> : -> Tabbed code means that any new variable is only useable within that scope

def sum(x, y):            # Parameters are the variables used in the function that represent the inputs
    x = 12
    y = 17
    total = x + y
    print(total)
    return x

x = 15
y = 17
print(sum(x, y))      # Arugments - Inputs into the function
x = sum(x, y)
print(x)    # 12

"""
function nthElement(n, lst) {
    for (var i=0; i<lst.length; i = i + n) {
        console.log(lst[i])
    }
}
"""

# Create a functon that returns every nth elements of a list
def nthElement(n, lst):
    items = []
    for i in range(n-1, len(lst), n):
        items.append(lst[i])
    return items

items = [1,2,3,4,5,6,7,8,9,10]
print(nthElement(2, items))
print(nthElement(5, items))

#Every 2 Element       -> [2,4,6,8,10]
#Every 3 Element       -> [3,6,9]

#--------------------------------------------------------------------------------------------------------------------------------------

# Classes - Instances | Blueprint -> Data Structure 
# Properties/ Instance Variables
# Functions - Constructor -> Set your properties | First function that gets run on initilization
# Getters - Retrieves a specific property | Setters - Sets a specific property


"""
class Car() {
    constructor() {
        this.year = 0
        this.color = ''
        this.make = ''
        this.model = ''
    }
}

"""

class Car():
    def __init__(self):
        self.year = 0
        self.color = ''
        self.model = ''

    def getYear(self):
        return self.year

    def setYear(self, year):
        self.year = year


car1 = Car()                # Objects or an Instance of Classes
print(car1.getYear())
car1.setYear(2001)
car2 = Car()

"""
class Toyota(Car):          # Subclassing means to extend a class's functionality with another
    def __init__(self):
        self.type = 'Truck'

    def getType(self):
        return self.type

truck1 = Toyota()
truck1.getType()
truck1.setYear()
"""

class Square():             
    def __init__(self, base, height):
        self.area = base * height

    def getArea(self):
        return self.area

sqr1 = Square(5, 2)         # Creating a new instance of a class you can pass in arguments to the constructor
sqr1.getArea()


#--------------------------------------------------------------------------------------------------------------------------------------

# Coding Patterns
# Frequency Pattern
def exFreqCounter(str):
    letters = {}
    for i in range(0, len(str)):
        currentLetter = str[i]
        if not currentLetter in letters:
            letters[currentLetter] = 1
        else:
            letters[currentLetter] += 1

    return letters

str = 'apple'      
exFreqCounter(str)       # {'a':1, 'p':2, 'l':1, 'e': 1}

# Max/Min
def maxCategory(genres):
    max = 0
    category = ''
    for genre in genres:
        count = genres[genre]
        if count > max:
            max = count
            category = genre

    return category

genres = {'adventure': 3, 'action': 4, 'horror': 3}
maxCategory(genres)         # action

# Linear Search
def linearSearch(searchTerm, food):
    for i in range(0, len(food)):
        currentFood = food[i]
        if currentFood == searchTerm:
            return i

linearSearch('apple', ['bannana', 'grapes', 'apple', 'oranges', 'melons'])

#--------------------------------------------------------------------------------------------------------------------------------------

# HTTP Protocol - The underlying communication method of the web
# Verbs - Actions on the Network | Ex. GET - Retrieves Data | POST - Creates Data | PUT - Updates Data | Delete - Deletes Data 
# Endpoint - The 'address' or the location of the resource you are trying to get to | Ex./contact | Ex2. /
# Headers - Description information about the request/response | Ex. content-type: application/json
# Status Codes - A code in a request or response that shows if everything worked or not | 200 - Success Message | 400 - Client Side Errors | 500 - Backend Error  
# Payload - Data you send in a request

# REST -> An architecture -> How you code your web communication using HTTP protocol
# Framework - A collection of libraries for a specific task | Ex. Web Framework -> Flask is used to build REST APIs

# Package Managers - Repositories for libraries
# Pre-Step - Install the modules you need -> pip install flask

# 1 import libaries/modules

# Flask - The main class of flask library that gives your application the powers of flask
# jsonify() - Converts a dictionary to JSON for use in a route
# render_template()  - Converts an HTML template to XML
# request() - Views the details of the request | Ex. Headers, Origin, Payload, Status Code, Arguments

from flask import Flask, jsonify, render_template, request

# 2 - Create a new instance of Flask
ali = Flask(__name__)

# 3 - Create your routes

# API Router
# Every flask route needs an endpoint, a method and a function
# Every flask function has to return JSON or HTML/XML
@ali.route('/home', methods=['GET'])
def start():
    return jsonify({'status': 'success'})

# API Route
@ali.route('/sum', methods=['GET'])
def sum():
    x = request.args.get('x')
    y = request.args.get('y')
    total = int(x) + int(y)
    return jsonify({'total': total})

# View Route
@ali.route('/examplePage', methods=['GET'])
def examplePage():
    return render_template('index.html')

# 4 - Start the flask server
# Optional Arguments
# debug=True -> Restarts the flask server when you make any change
# port=4888 -> Update the default port of 5000 to 4888
ali.run(debug=True, port=4888)



# Network Terms

# Public IP - ATT -> Connect to the outside world           | Ex. 99.98.101.60
# Network IP -> Internal Network Addresses from your router | Ex. 172.29.112.1
# Localhost - A default IP address for your local computer -> 127.0.0.1

# Port - A dock where an app can exist and connect to the internet |(SMTP) Email - Port 22| HTTP - Port 80 | Flask - Port 5000 | MongoDB - Port 27017
# Router - A tool to create a network, and navigate to other devices
# Domain Name - Human Readable web address | Ex. Google
# DNS - Takes in a domain and looks up the IP address for it
# DHCP - Assigns IP addresses