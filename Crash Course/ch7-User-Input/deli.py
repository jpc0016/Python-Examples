# CH7 Exercise 7-8
#
# deli.py
#
# Make a list called sandwich_orders and fill it with various sandwiches
# Move each sandwich in sandwich_orders to an empty list called finished_sandwiches
# When all sandwiches are moved, print a message listing each sandwich that was made.
sandwich_orders = ['hero', 'blt', 'meatball', 'turkey', 'roast beef']
finished_sandwiches = []

# Loop through sandwich_orders and print a message for each order
for sandwich in sandwich_orders:
    # Capitalize BLT
    if sandwich == 'blt':
        print("I made your " + sandwich.upper() + " sandwich.")
    else:
        print("I made your " + sandwich.title() + " sandwich.")

    # Add to finished_sandwiches. Add sandwich with proper format.
    if sandwich == 'blt':
        finished_sandwiches.append(sandwich.upper())
    else:
        finished_sandwiches.append(sandwich.title())



print("\n---Sandwiches Made---")
for item in finished_sandwiches:
    print(item)
