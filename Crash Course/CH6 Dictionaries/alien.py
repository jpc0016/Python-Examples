# CH6 Example
#
# alien.py
#
# simple dictionary that stores information about a particular alien
# dictionaries store key:value pairs that have particular relations
alien_0 = {'color': 'green', 'points': 5}

# print indexed values
# print(alien_0['color'])
# print(alien_0['points'])

# If a player shoots down an alien, you can look up how many points they should earn:
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Add new key:value pairs for the alien:  x and y coordinates
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
