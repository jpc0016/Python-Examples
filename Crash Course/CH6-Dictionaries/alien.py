# CH6 Example
#
# alien.py
#
# simple dictionary that stores information about a particular alien
# dictionaries store key:value pairs that have particular relations
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# Create a list of dictionaries
# aliens = [alien_0, alien_1, alien_2]
#
# # Print each alien's attributes
# for alien in aliens:
#     print(alien)

# print indexed values
# print(alien_0['color'])
# print(alien_0['points'])

# If a player shoots down an alien, you can look up how many points they should earn:
# new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points!")

# Add new key:value pairs for the alien:  x and y coordinates
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# Create a fleet of 30 aliens

## empty alien list
aliens = []

# Create the 30 aliens
for i in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
# len() is not an attribute/method.  Use str(len($item)) to find length
print("Total number of aliens: " + str(len(aliens)))

# Change the first three aliens to yellow type from green if they are hit
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    # if alien is already yellow change to red
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)
