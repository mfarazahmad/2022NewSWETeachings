# Primitive Data Types

# Strings | Integers | Booleans

name = "Faraz"
age = 12
isTrue = True

# Data Structures - Container Data

# -------- Dictionary | Array ------

# Arrays (Lists) are great for list data
names = ["joe","bob","flob"]
# Accessing an element of an array | Access by its index
print(names[1])

# Dictionary (Hashmaps) is for descriptive data in the form of a key value pair
car = {'make': "Toyota", 'model': 'Camry', 'year': 2000}
# Accessing an element of an dictionary | Access by its key
print(car['model'])

# String formatting - Start with f and put quotes and then curly bracket for python syntax
# len() - A built in function that finds the length of the items in the data structure
print(f"The number of car owners: {len(names)}")
print(f"The number of letters in my name: {len(name)}")


# ----------------------------------------- 

# Function - A piece code that is resuable and has a specific purpose

"""
Encapsulation:  
- Hiding the functionality of code. 
- Limiting a code's use to one little area

Scope - The accessbility of a variable within an area is its scope
""" 

num1 = 25
num2 = 100
total = num1 + num2

print('------- EXAMPLE 1-----')
# Ex. 1 - Basic Sum Function
def sum():      # A piece of code that will add two numbers
    num1 = 15
    num2 = 72
    total = num1 + num2
    print(f"My total 1 is {total}")

# Total 1 is only within scope of the sum function
sum()
# Total 2 is only within scope of the entire document
print(f"My total 2 is {total}")

print('------- EXAMPLE 2-----')
# Arguments | Parameters
# Ex. 2 - Sum Function with Parameters

def sum(num1, num2):        # Parameters - The variables that take in the data passed
    total = num1 + num2
    print(f"My total is {total}")

sum(5, 7)                   # Arguments - The data being passed in to the function
sum("faraz", "khuzaima")

print('------- EXAMPLE 3-----')
# Ex. 3 - Sum function w/ Parameters & a type check to enforce integer
def sum(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        total = num1 + num2
        print(f"My total is {total}")
    else:
        print("Please enter in a number!")

sum(5, 7)               
sum("faraz", "khuzaima")
sum(5, "faraz")


# Create 5 students that have each a name, age, grade | CHECK :D
# Create a function that adds the ages of all the students

# HW
# Create a function that adds the grades of all the student
# Bonus - Add in addtional logic to determine which student has the highest grade

allages=0
# print(students[0]['age'])
def sumOfAges(data, total): 
    for i in range(0,len(data)):
        total += int(data[i]['age'])
    return total

bestStudents = [
    {'name': 'Faraz',       'age': "5",     'grade':"10"},
    {'name': 'Khuzaima',    'age': "20",    'grade':"3"},
    {'name': 'Bob',         'age': "19",    'grade':"7"},
    {'name': 'Rakin',       'age': "13",    'grade':"8"},
    {'name': 'Kamran',      'age': "23",    'grade':"12"}
 ]

worstStudents = [
    {'name': 'Bob',       'age': "17",     'grade':"10"},
    {'name': 'Dick',    'age': "2",    'grade':"3"},
    {'name': 'Rich',         'age': "11",    'grade':"7"},
    {'name': 'La',       'age': "15",    'grade':"8"},
    {'name': 'Charzard',      'age': "6",    'grade':"12"}
 ]

bestSumAges = sumOfAges(bestStudents, allages) 
print(bestSumAges)
#sumOfAges(worstStudents) 

sum = 5 + 10
# Error Handling
# What Types of Errors | NameError, SyntaxError, IndexError, KeyError, TypeError


# Built In Functions for Python
# print(data) - allows you to display variables, data, logic into the terminal for diagnosing
# range(start, end) - makes a number between a start and end
# len(arr) - Arrays & Strings -> How many items or characters are in the array or string
# input() - That allows values in from the terminal as a string



nflTeams = [
    {'headquarters': 'Atlanta', 'name': 'Falcons', 'nickname': 'Dirty Birds', 'conference': 'NFC', 'division': 'South', 'established': '1966',
    'colors': 'black, red, silver, white', 'mascot': 'Freddie'},
    {'headquarters': 'Baltimore', 'name': 'Ravens', 'nickname': 'Purple Pain', 'conference': 'AFC', 'division': 'North', 'established': '1996',
    'colors': 'purple, black, gold', 'mascot': 'Poe'},
    {'headquarters': 'Denver', 'name': 'Broncos', 'nickname': 'Orange Crush', 'conference': 'AFC', 'division': 'West', 'established': '1959',
    'colors': 'orange, blue, white', 'mascot': 'Miles'},
    {'headquarters': 'Seattle', 'name': 'Seahawks', 'nickname': 'Legion of Boom', 'conference': 'NFC', 'division': 'West', 'established': '1974',
    'colors': 'navy, green, grey', 'mascot': 'Blitz'},
    {'headquarters': 'Philadelphia', 'name': 'Eagles', 'nickname': 'Iggles', 'conference': 'NFC', 'division': 'East', 'established': '1933',
    'colors': 'green, black, silver, white', 'mascot': 'Swoop'}
]

# 5. Find the colors of each team using input():
# Try to get the colors for a team to print after inputting the team's name.


print("Enter a team name: ")
userTeamName = input()
isFound = False

for i in range(0, len(nflTeams)):
    if userTeamName == nflTeams[i]['name']:
        print(nflTeams[i])
        isFound = True

if not isFound:
    print("Could not find your team!")


controls = """
    CONTROLS:
    1 - First Option
    2 - Second Option
    3 - Third Option
    4 - Blank Look
"""

def introStory():
    print("""
        \n
        You are a peasant in a village far away named Stuey.
        You are a labor worker struggling to make ends meet working in a coal mind.
        A war starts and the economy breaks down and coal miners are no longer needed.
        He becomes dirt poor and desperate.
        He only has a few options before him......
        \n
        Adventure:
        You decide to become a con artist to swindle the richest business man lawyer in the city named Peter Griffin.
        Your hope of marrying his daughter and taking his wealth.
    """
    )

def expertPath():
    print("""
        You hear about a man in the city that is an expert and he as the choice to learn under him for a few years.
        Would you like to learn from him. (Yes or No)
    """)

    choice = input()

    if choice == '1':
        return True

    return False

def careerChoice(isExpert):
    print('Peter: Hello Charles, what is your background sir that your dare speaketh my name! | Thief, Blacksmith, BEST OPTION: Politician')
    choice = input()

    if choice == '1':
        print("For daring to speak with him, your are hung up by your testicales in the street right then and there.")
        print('YOU DIED!')
    elif choice == '2':
        blackSmithRoute()
    elif choice == '3' and isExpert:
        politicanRoute()
    elif choice == '3' and not isExpert:
        print("For daring to speak with him, your are hung up by your testicales in the street right then and there.")
        print('YOU DIED!')
    elif choice == '4':
        print("For daring to speak with him, your are hung up by your testicales in the street right then and there.")
        print('YOU DIED!')

def blackSmithRoute():
    print("""
    Blacksmith Route
    - Peter Intrigued: Oh a blacksmith eh. Quick boy what business do yo have with me.
    - I am reknown blacksmith and have made many famous swords. Even that of King Khuzaima the third Protector of the realm and my anus.

    """)

    print("""
        Here is my proof |  Have a fellow begger dressed richly to fool him | Has a sword with paint to fool him
    """)

    choice = input()
    if choice == '1':
        print('- Present a rich guy you as proof that he knows of the king that can attest to this.')
        print('HURRAH YOU GOT THE Money but no girl!')
    elif choice == '2':
        print('Peter: You DARE lie to me bastard. You will be flogged on the streets and sent to mine in the deserts with the rapists for the rest of your life.')
        print('YOU DIED!')

def politicanRoute():
    print('ERROR: We have not coded this yet. But suffice to say you got the money and the girl!')

def storyProgression():
    print(controls)
    print("Enter in h as the prompt to display controls if lost")
    introStory()
    # A boolean to keep track of whether this guy is an expert
    isExpert = expertPath()
    print(isExpert)
    careerChoice(isExpert)


storyProgression()