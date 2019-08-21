# CH10 Example
#
# number_writer.py
#
# Storing data using the JSON module. JSON allows for storage of simple data
# structures for later use. JSON is also not exclusive to Python. Can be used
# in JavaScript instances
import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
