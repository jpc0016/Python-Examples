# CH6 Example
#
# pizza.py
#
# Can place lists inside of dictionaries
# Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order
print("You ordered " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")
# print the toppings list with a for-loop
for topping in pizza['toppings']:
    print("\t" + topping)
