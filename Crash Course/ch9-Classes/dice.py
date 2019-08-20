# CH9 Exercise 9-14
#
# dice.py
# August 20, 2019
#
# Make class called Die() with an attribute, sides, with default value of 6.
# Make roll_die() method that prints random number between 1 and number of sides
# the die has.  Roll 6-side, 10-side, and 20-side die 10 times each
from random import randint

class Die():
    """Class that simulates a dice object"""

    def __init__(self, sides=6):
        """Initialize Die attributes"""
        self.sides = sides

    def roll_die(self):
        """Prints random number between 1 and number of sides"""
        result = randint(1, self.sides)
        print(str(result))

# Rolling a standard 6-sided dice
standard = Die()
x = 1
while (x < 11):
    standard.roll_die()
    x += 1

print(" ")

# Rolling a 10-sided dice
ten_sides = Die(10)
y = 1
while (y < 11):
    ten_sides.roll_die()
    y += 1

print(" ")

# Rolling a 20-sided dice
D_and_D = Die(20)
z = 1
while (z < 11):
    D_and_D.roll_die()
    z += 1
