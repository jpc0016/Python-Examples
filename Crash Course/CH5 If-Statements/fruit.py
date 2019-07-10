# CH5 Exercise 5-7
#
# Favorite Fruit
# Make a list of favorite fruits then write an if-statement to check for
# certain fruits in the list

# Create the list of fruits
favorite_fruits = ['apples', 'bananas', 'grapefruit']

# Check for singular and plural fruits
# This prints
if 'apple' in favorite_fruits or 'apples' in favorite_fruits:
    print("You really like apples!")

if 'pear' in favorite_fruits or 'pears' in favorite_fruits:
    print("You really like pears!")

# This prints
if 'grapefruit' in favorite_fruits:
    print("You really like grapefruit!")

if 'grape' in favorite_fruits or 'grapes' in favorite_fruits:
    print("You really like grapes!")

# This prints
if 'banana' in favorite_fruits or 'bananas' in favorite_fruits:
    print("You really like bananas!")
