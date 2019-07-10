# CH5 Exercises 5-4 & 5-5
#
# Alien colors game #2 and 3

# 5-4
# Create a variable alien_color and assign it 'green', 'yellow', or 'red'
alien_color = 'green'

# This version runs the if-block
if alien_color == 'green':
    print("You earned 5 points!")
else:
    print("You earned 10 points!")


# This version runs the else-block
alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points!")
else:
    print("You earned 10 points!")

# Spacing for next exercise
print("")
print("")
print("")

# 5-5
# Turn 5-4 into an if-elif-else chain
# alien_color = yellow from previous example
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

# green test
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")


# red test
alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")
