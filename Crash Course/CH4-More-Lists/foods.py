# CH4 List Copying
# foods.py

my_foods = ['pizza', 'falafel', 'carrot cake']

# make list copy using only one colon
friend_foods = my_foods[:]

# append individual foods to each list to prove list difference
my_foods.append('sushi')
friend_foods.append('steak')

# setting lists equal to eachother is not "list copying".
# the below sets has both lists pointing to the same memory location so that
# a change in one list will alter the other.
# friend_foods = my_foods

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
