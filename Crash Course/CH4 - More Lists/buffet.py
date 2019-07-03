# CH4 Tuple exercise 4-13
#
# buffet.py
# store 5 simple foods in a Tuple
chipotle = ('chicken', 'rice', 'tomato', 'beans', 'cheese')

print("The chipotle ingredients are below:")
for food in chipotle:
    print(food)

# Cannot append below since chipotle is a tuple
# chipotle.append('steak')

# rewrite the tuple to replace two of the menu items
chipotle = ('steak', 'rice', 'avocado', 'beans', 'cheese')

# use a for loop to print each item of revised menu
print("\nThe updated ingredients are below:")
for ingredient in chipotle:
    print(ingredient)
