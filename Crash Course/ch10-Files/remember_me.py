# CH10 Example
#
# remember_me.py
#
# Saving and Reading User-Generated Data
# Prompt user for their name and remember it the next time they run the program
import json

# Refactored code by moving it into a function, greet_user()
def greet_user():
    """
    Try opening username.json and loading contents into username
    If username.json does not exist, create it and write a username to it
    """
    filename = 'username.json'
    username = get_stored_username(filename)
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username(filename)

# Refactor the file existence check by creating get_stored_username()
def get_stored_username(filename):
    """Get a stored username if it exists"""

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

# Refactor block that creates new username
def get_new_username(filename):
    """Prompts for a new username if one does not exist"""
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print("We'll remember you when you return, " + username + "!")
    return username

# Call main function, greet_user()
greet_user()
