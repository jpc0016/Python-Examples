# CH4 Slices exercies 4-10, 4-11, and 4-12
#
# Exercise 4-10:
# Use the list-slice.py code
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# Print first 3 items in list
print("Here are the first three players on my team:")
for player in players[:3]:
  print(player.title())

# print middle 3 items in list
print("\nHere are the middle three players on my team:")
for player in players[1:4]:
  print(player.title())

# print last 3 items in list
print("\nHere are the last three players on my team:")
for player in players[2:]:
  print(player.title())

# Exercise 4-11
# use code from pizza.py.  Make copy of pizzas list and call it friend_pizzas
pizzas = ['cheese', 'pepperoni', 'supreme']

# list copy
friend_pizzas = pizzas[:]

# add new pizza type to friend_pizzas
friend_pizzas.append('sausage')

# prove the two lists are different
print("\nMy favorite pizzas are: ")
for pizza in range(0,len(pizzas)):
    print(pizzas[pizza])

print("\nMy friend's favorite pizzas are: ")
for pizza in range(0,len(friend_pizzas)):
    print(friend_pizzas[pizza])
