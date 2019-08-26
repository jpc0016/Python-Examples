# CH15 Example
#
# die.py
#
# Introduction to Pygal
# Simulate a die rolling and return a random number
from random import randint

class Die():
    """A class representing a single die"""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """return a random value between 1 and num_sides"""
        return randint(1, self.num_sides)
