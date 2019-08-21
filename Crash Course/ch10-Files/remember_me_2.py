# CH10 Exercise 10-13
#
# remember_me_2.py
#
# Modify remember_me.py in case the current user is not the person who last
# used the program.  Before printing a welcome back message in greet_user(), ask
# if this is correct username.  If not, call get_new_username() to get correct one
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
        prompt = input("Is " + username + " the correct username? (y/n)  ")
        if prompt.lower() == 'y':
            print("Welcome back, " + username + "!")
        elif prompt.lower() == 'n':
            get_new_username(filename)
        else:
            print("Please answer 'y' or 'n'")
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
