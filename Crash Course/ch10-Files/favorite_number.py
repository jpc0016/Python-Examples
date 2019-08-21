# CH10 Exercise 10-11
#
# favorite_number.py
#
# Prompt user for their favorite number and dump it to a json file. Write a
# separate file that reads it and prints a display
import json

filename = 'numbers.json'

with open(filename, 'w') as f:
    number = input("What is your favorite number? ")
    json.dump(number, f)
    f.close()
