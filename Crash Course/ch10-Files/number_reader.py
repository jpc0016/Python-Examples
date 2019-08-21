# CH10 Example
#
# number_reader.py
#
# Read data using json.load() method. It takes only one parameter: the file object
import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

#print(numbers)
# This line is for reading Exercise 10-11
print("I know your favorite number! It's " + str(numbers) + ".")
