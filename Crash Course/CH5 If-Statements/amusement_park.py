# CH5 Example - if/else statements
#
# amusement_park.py
#
# Determine ticket price based on a customer's age
age = 12

# pass age into the if-statement to determine price
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your ticket price is $" + str(price) + ".")
