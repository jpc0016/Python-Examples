# CH5 Multiple lists example
#
# Check for unusual toppings requests
#
# Populate two lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# loop through requested toppings list
for topping in requested_toppings:
    # compare requested topping to available toppings to filter unusual toppings.
    if topping in available_toppings:
        print("Adding " + topping + ".")
    else:
        print("Sorry, we don't have " + topping + ".")

print("\nFinished making your pizza!")
