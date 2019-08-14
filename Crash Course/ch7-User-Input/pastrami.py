# CH7 Exercise 7-9
#
# pastrami.py
#
# Using sandwich_orders from 7-8, add "pastrami" at least three times.
# Print a message saying the deli ran out of pastrami
# Use a while loop to remove all instances of pastrami from the list
sandwich_orders = ['hero', 'blt', 'meatball', 'turkey', 'roast beef', 'pastrami', 'pastrami', 'pastrami', 'pastrami', 'pastrami']

print("\nThe deli has run out of pastrami!  We cannot serve that sandwich!  ")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(" ")
print(sandwich_orders)
