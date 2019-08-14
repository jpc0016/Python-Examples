# CH6 Exercise 6-10
#
# Favorite Numbers Part 2
# favorite_numbers_2.py
#
# Modify Exercise 6-2 to include more than one favorite number
# Use a dictionary to store people's numbers.

# Define the dictionary with values defined as lists
numbers = {
    'Jeff': [8,9,10],
    'Mark': [13],
    'Danesh': [69],
    'Richard': [10, 11, 4, 12, 599],
    'Wang': [5555515, 314, 1],
}

# print each person's name with their favorite number
for name, number in numbers.items():
    if len(number) == 1:
        # Use .strip("[]") to remove brackets from single numbers.  This is a str.strip() method
        # and works because the number is already converted to a string --> str(number)
        print("\n" + name.title() + "'s favorite number is " + str(number).strip("[]") + ".")
    else:
        print("\n" + name.title() + "'s favorite numbers are: ")
        for item in number:
            print("\t" + str(item))
