# Backend: Wrote Some Code that retrieves customer billing info from a database

# User Interface: Displays Some Information billing info

# Testing - Usable Data | Name | Credit Card | Insurance | Salary | Address

# Modeling - Means creating data to match whats in real life

# Build Data -> Generate Data

# VENDOR

"""
GOAL - Build a Dashboard that allow me to see my vendors

------ Data Model -------

VENDOR
    Name
    PRODUCT
        Prices
        Names
        Images
        Taxes
        Description
        Inventory
    CONTACT INFO
        Name
        Email
        Phone
        Contact 2:
        Type:
    SHIPPING
        Delivery TimeFrame
        Delivery POC
        ADDRESS
            Zip
            State
            Street
    REVIEWS
        USER
            Name
            Email
            Pass
        Date
        Score
        Description

PURCHASE HISTORY
    Date of Sale
    PRODUCT
        Prices
        Names
        Images
        Taxes
        Description

"""  

# Primitive Data -  Store in a variable
isEnabled = True        # Boolean
name = "Faraz"          # String
age = 30                # Integer

# Built-In Data Structures - Stores in their own containers
names = ['Bob', 'Joe', 'Zack']                                  # Array
cars = {'make':'Honda', 'year': '2010', 'model': 'accord'}      # Dictionary

# Functions - Container of Logic | Performs operations on Data
def sumOf5():
    total = 5 + 5
    return total

sumOf5()

# Classes - Containers of Data & Logic
class Product():
    def __init__(self):
        self.price = 0
        self.name = ""
        self.images = []
        self.taxes = ""
        self.description = ""
        self.inventory = ""

    def getPrice(self):
        return self.price

    def setPrice(self, update):
        self.price = update

    def getInventory(self):
        return self.inventory

    def setInventory(self, update):
        self.inventory = update

apple = Product()
apple.setInventory(5)
print(apple.getInventory())

bananna = Product()



# -------------------------------------------------------------


# Create a function that can generate any product randomly | Use Arrays  | Dictionaries
"""
PRODUCT
    ID
    Price
    Names
    Tax
    Inventory
"""

import random   # Libraries/Modules

#print(f"The random number is: {random.randint(0, 5)}")

"""
# IDEA STATION TO USE RANDOM
Generate ID 
Randomize Names | [a,b,c,d,e,f,g,h,i,j,k,l,m,n]
Randomize Price | 10.00
"""

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','v','x','y','z']
randomNum = random.randint(0, len(letters))
print(randomNum)
print(letters[randomNum])

def generateProduct():
    # Generating Below Data Structure From other Data Structures
    product = {'name': 'apple', 'price': 5}
    return product

vendorNames = ['farm1', 'farm2', 'farm3', 'farm6', 'farm7']

def generateVendor():
    vendor = {}

    # Generate name
    name = 'Joe'
    vendor['name'] = name

    products = []
    for i in range(0, 5):
        products.append(generateProduct())
    vendor['product'] = products
    
    print(vendor)

generateVendor()