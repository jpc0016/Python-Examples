# CH6 Example
#
# languages.py
#
# Track favorite programming languages for users and print a
# favorite one.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# Typically break up longer print statements after "+" sign
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")
