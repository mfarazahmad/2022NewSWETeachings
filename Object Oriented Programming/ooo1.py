# Data Stores
# Strings, Tuples, Integers, Booleans
# Basic Data Structure: Dictionaries, Arrays

# Dictionary - Holds Description Data in a Key-Value Pair
# Arrays - Holds Data in a List

# Functions - Performs a task (preferably one small task)
# 
"""
Examples: 
len(arr) - Counts the number of items in a list or string
random.randInt(int) - Creates a number between 0 and 1.
input(str) - Takes in a user input from the terminal

sum(x,y) - Add two numbers
highestGrade(arr) - Find the highest grade given data
avgAge(arr) - Find the average age of the data
triangleArea(base, height) - Found the area of triangle
generateName() - Make a random name

change(function()) - Call Back Function -> When something is changed in the element do something
click(function()) - Call Back Functions - When something is clicked do something
""" 

# ------ Classes -------
# Class is a blueprint that can be self replicated to represnt something
# Properties - Data to Describe itself
# Functions - To Do Stuff to the data | Getters and Setters - Get Properties out and set properties in the class


# Example. GM you are building an app that takes in data about a bunch of cars

"""
Car
    Make            string
    Model           string
    Year            integer
    Color           string
    Price           float
    Accessories     array of strings

    getMake()
    setMake()
    
    getModel()
    setModel()

    getYear()
    setYear()

    getColor()
    setColor()
    
    getAccessories()
    getPrice()

    calculateTax(taxRate)
    addAccessory(itemName)
"""

from pydoc import pager


class Car():
    # Constructor - Intialization Function that gets run every time a new car is made
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.year = 0
        self.color = ""
        self.accessories = []
        self.price = 0

    def getMake(self):
        return self.make
    def setMake(self, make):
        self.make = make

    def getModel(self):
        return self.model
    def setModel(self, model):
        self.model = model

    def getYear(self):
        return self.year
    def setYear(self, year):
        self.year = year

    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color
    
    def getAccessories(self):
        return self.accessories
    def getPrice(self):
        return self.price


# Creating an object | Creating an instance/version of Car Class
car1 = Car("Honda", "Civic")
print(car1.getMake())
car1.setYear(1988)

car2 = Car("Audi", "R8")
print(car2.getMake())

cars = [car1, car2]

"""
Customer
    name 
    ban
    email 
    phone
    creditCard
    cvv

    getCurrentBill()


    Plan 
        price
        name
        Line
            Phone
                name
                simcard
                price
    Features
        name
        price
        bonunes
"""