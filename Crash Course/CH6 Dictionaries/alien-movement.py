# CH6 Example
#
# Modifying values in a dictionary
# alien.py
#
# Track the position of an alien that can move at different speeds
# Create alien_0 dictionary with x, y, and speed
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original X position: " + str(alien_0['x_position']))

# Move alien to the right
# Determine how far to move alien based on current speed.  Store in variable
# x_increment and add it to latest x_position
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien!!!!
    x_increment = 3

# Increment current x position based on output of if-statement
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New X position: " + str(alien_0['x_position']))
