# Two More Examples of A Data Model

# Purchase History
"""
PurchaseHistory 
    date/time
    total
    transactionID
    Payment
        cardnumber
        exp
        cvv
    Product
        name
        quantity
        price
    User
        username
        Address
            street
            state
            zip
        contact
"""
class Address():
    def __init__(self):
        self.street = ""
        self.state = ""
        self.zip = 0

    def getStreet(self):
        return self.street
    def setStreet(self, street):
        self.street = street
    
    def getState(self):
        return self.state
    def setState(self, state):
        self.state = state
    
    def getZip(self):
        return self.zip
    def setZip(self, zip):
        self.zip = zip

print("----ADDRESS----")

address1 = Address()
address1.setStreet("123 chicken lane")
print(address1.getStreet())

class User():
    def __init__(self):
        self.username = ''
        self.address = None
        self.contact = ''

    def getUsername(self):
        return self.username
    def getAddress(self):
        return self.address
    def setAddress(self, address):
        self.address = address

    def getContact(self):
        return self.contact
    def setContact(self, contact):
        self.contact = contact

print("----USER----")

user1 = User()
user1.setAddress(address1)
print(user1.getAddress().getStreet())

# Calculator
class Calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def getNum1(self):
        return self.num1
    def setNum1(self, num1):
        self.num1 = num1

    def getNum2(self):
        return self.num2
    def setNum2(self, num2):
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def divide(self):
        return self.num1 / self.num2
    def multiply(self):
        return self.num1 * self.num2

print("----CALCULATOR----")

problem = Calculator(5, 2)
print(problem.multiply())
print(problem.add())

problem.setNum1(7)
problem.setNum2(8)
print(problem.getNum2())
print(problem.multiply())


# Game of War - Coding Challenge
    # A game that has two players a deck of cards
    # Rules: Compares who has highest card. If the card has the same value its war
    # Rule2: Then compares who has highest card.
    # Win: Highest Card Wins!
    # Keep going until one person loses all their cards
import random

class Card():
    def __init__(self, suite, number):
        self.suite = suite
        self.number = number

    def getSuite(self):
        return self.suite

    def getNumber(self): 
        return self.number


class Deck():
    def __init__(self):
        self.deck = []

        suites = ["diamond", "clubs", "hearts", "spades"]
        numbers = [x for x in range(1,14)]
        print(numbers)

        for suite in suites:
            for number in numbers:
                newCard = Card(suite, number)
                self.deck.append(newCard)
        
    def length(self):
        return len(self.deck)

    def getDeck(self):
        newDeck = []
        for i in range(0,len(self.deck)):
            card = self.deck[i]
            dictCard = {"suite": card.getSuite(), "number": card.getNumber()}
            newDeck.append(dictCard)
        
        self.deck = newDeck
        return newDeck

    def shuffle(self):
        print(random.shuffle(self.deck))

print("----GAME OF WAR----")

deck1 = Deck()
print(deck1.length())
#print(deck1.getDeck())
    
#deck1.shuffle()

""" 
Deck
    length
    Cards
        suits
        numbers

"""