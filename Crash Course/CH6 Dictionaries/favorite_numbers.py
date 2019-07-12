# CH6 Exercise 6-2
#
# Favorite Numbers
# favorite_numbers.py
# Use a dictionary to store people's numbers.

# Define the dictionary 
numbers = {
    'Jeff': 8,
    'Mark': 13,
    'Danesh': 69,
    'Richard': 10,
    'Wang': 5555555,
}

# print each person's name with their favorite number
for item in numbers:
    print(item + "'s favorite number is " + str(numbers[item]) + ".")
