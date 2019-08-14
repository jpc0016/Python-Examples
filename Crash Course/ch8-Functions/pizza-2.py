# CH8 Example
#
# pizza-2.py
#
# Passing arbitrary number of arguments.
# Start with pizza.py

# The * tells Python to create an empty tupple called 'toppings' and stick whatever values
# are received into that tupple.  Parameters that accept arbitrary amount of arguments must
# be placed at the end of the list
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested"""
    print("\nMaking a " + str(size) + "\" pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping.title())

make_pizza(16, 'pepperoni')
make_pizza(12, 'pineapple', 'sausage', 'anchovies')
