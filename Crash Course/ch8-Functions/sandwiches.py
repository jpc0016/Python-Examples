# CH8 Exercise 8-12
#
# sandwiches.py
#
# Write a function that accepts a list of items a person wants on their sandwich.
# One parameter that collects as many items provided
# Print a summary of the sandwich being ordered
def sandwich_items(*toppings):
    """
    Print a summary of the sandwich items provided
    """

    print("\nSandwich Items: ")
    for topping in toppings:
        print(topping.title())

sandwich_items('lettuce', 'tomato', 'pickles')
sandwich_items('mayo')
sandwich_items('jalapenos', 'ketchup', 'cheese')
