# CH5 Check for Special Items
#
# pizzeria.py
#
# Built from toppings.py
# Make a loop to announce each topping added to the pizza
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#
# # check for green peppers before adding them to pizza
# for topping in requested_toppings:
#     if topping == 'green peppers':
#         print("Sorry, but we're out of green peppers.")
#     else:
#         print("Adding " + topping + " to your pizza!")
#
#
# print("\nDone making your pizza!\n")


# Checking that a list is not empty

# Create empty toppings list
requested_toppings = []

# When the name of a list is used in an if statement, Python returns True if the list con-
# tains at least one item; an empty list evaluates to False.
if requested_toppings:
    for topping in requested_toppings:
        print("Adding " + topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
