

# Write a dictionary and count the number of each letter
letter_counter = {}
state = 'mississippi'
for i in range(0, len(state)):
    letter = state[i]
    if letter in letter_counter:
        letter_counter[letter] += 1
    else:
        letter_counter[letter] = 1

'''
Write a Python program to compute the difference between two lists.

# Khuzaima Solution
color1 =  ["red", "orange", "green","blue","white"]
color2= ["black","yellow","green","blue"]
print(color1)

for i in range(0,len(color1)):
    calculate1 = color1[i]
    if calculate1 not in color2:
        print(calculate1)

Test Data:
["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]

Expected Output:
Color1-Color2: ["white", "orange", "red"]
Color2-Color1: ["black", "yellow"]
'''

arr1 = ["red", "orange", "green", "blue", "white"]
arr2 =  ["black", "yellow", "green", "blue"]

rejects = []
for i in range(0, len(arr1)):
    arr1_color = arr1[i]
    print('Loop 1')
    print(f"Color {i+1} from arr1 is: {arr1_color}")

    isColor = False
    for j in range(0, len(arr2)):
        print("Loop 2")
        arr2_color = arr2[j]
        print(f"Color {j+1} from arr2 is: {arr2_color}")

        # If the colors do match
        if arr1_color == arr2_color:
            isColor = True

    if not isColor:
        rejects.append(arr1_color)
        print(f'reject added {arr1_color}')

    print('\n')


print(rejects)




# How to find one color
red = arr1[0]

rejects = []
for i in range(0, len(arr2)):
    arr2_color = arr2[i]
    print(f"Color {i+1} from arr2 is: {arr2_color}")
    # If the colors do not match
    if red != arr2_color:
        rejects.append(red)



"""
THOUGHT PROCESS AREA
if arr1[0] == arr2[0]:

if arr1[0] ==  arr2[1]:

if arr1[0] ==  arr2[1]:

if red is in second box
is red black
is red yellow
is red green
is red blue 

if orange is in the second box
is orange black
is orange yellow
is orange green
is orange blue 

HELL NO

REJECT BOX = ["red", "orange"]

"""
# _____________________________________

"""
FIRST TIME LOOP 1 Is RUnning
i = 0
arr1 color = red

LOOP 2 is running complete
j = 0
arr2 color = black

j = 1
arr2 color = yellow

j = 2
arr2 color = green

j = 3 
arr2 color = blue


__________________
SECOND TIME LOOP 1 is running
i = 1

LOOP 2 is running complete
j = 0
arr2 color = black

j = 1
arr2 color = yellow

j = 2
arr2 color = green

j = 3 
arr2 color = blue
"""