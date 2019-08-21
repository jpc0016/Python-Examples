# CH10 Example
#
# greet_user.py
#
# Reading User-Generated Data
# Greet user whose name is alread stored
import json

filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
    print("Welcome back, " + username + "!")
