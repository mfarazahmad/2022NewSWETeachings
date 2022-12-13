# Frequency Counter - Is using a dictionary to count things. Ex Letters

# isAnagram - Create a function that determines if two strings are anagrams of eachother

"1. {} - Place your counts "

"2. Look inside your data structure - AKA Loop"

"3. Build your list of items that you are looking for, letters, movies, etc."

"3a. First time a item is run across, you make that a key and set count to 1"
"3b. If the item is in there add 1 to the count "

"O(n)"
def isAnagram(str1, str2):
    count = {}
    for i in range(0,len(str1)):
        letter = str1[i]
        if letter in count:
            count[letter] += 1
        elif not letter in count:
            count[letter] = 1

    count2 = {}
    for i in range(0, len(str2)):
        letter = str2[i]
        if letter in count2:
            count2[letter] += 1
        elif not letter in count2:
            count2[letter] = 1

    for letter in count:
        if not letter in count2:
            return False
        else:
            if count[letter] != count2[letter]:
                return False
    
    return True  

print(isAnagram("zaraf", 'faraz'))      # True
print(isAnagram("nikar", "rakin"))      # True
print(isAnagram("narmak", "kamrun"))    # False


# 2 Pointers - Create two variables that target different indexs in a string or array and you move both until they meet

# isPalindrome - Create a function that takes in one string and checks if its a palindromes

def isPalindrome(str1):
    start = 0
    end = len(str1) - 1

    for i in range (0, len(str1)):
        if start < end:
            if str1[start] == str1[end]:
                start += 1
                end -= 1
            else:
                return False
        else:
            break

    return True

print('----------------------------------------')

print(isPalindrome('madam'))
print(isPalindrome('ubt'))
# nun           letters repeat front and back | first index and last index are the same
# madam         first and last | second and last -1 | t
# racecar
# aabaa
# aba
# a
# ubt
"""
i - count which coincides with index

m       <- index 0 | start
a            1 + 1 = 2
d 
a            3 - 1 = 2    
m       <- index 4 | end | len(str1) - 1

"""

"Pointers are useful anytime you want to compare two or more items in the same list/string" 


"Place Pointers on Two different indices"
"First Index......Last Index"
"First Index....Second Index"


"We use i=0 to indicate the current index "
"Start Index: i=0 | Last Index: len(arr) - 1"

max = 0
grades = [50, 21, 32, 6, 90]

max = 0
end = 1
"Find the Max Grade"
for start in range(0, len(grades)-1):
    grade = grades[start]
    if grade > end:
        max = grade
    else:
        max = end
        end += 1