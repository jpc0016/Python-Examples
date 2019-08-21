# CH10 Exercise 10-12
#
# favorite_number_2.py
#
# Combine functions in favorite_number.py.  If number is already stored, report
# favorite number to user.  If not, prompt user for favorite number.
import json

filename = 'numbers.json'

# Check if numbers.json exists
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    # retrieve number and store in numbers.json if it does not exist
    number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
        f.close()
else:
    print("I know your favorite number! It's " + str(number) + ".")
