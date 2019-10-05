# CH15 Example and Exercises 15-4 and 15-5
#
# random_walk.py
#
# Generate random data by creating a RandomWalk() class.  This will be imported
# by rw_visual.py to plot the random walk points.
from random import choice

class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # all walks start at (0, 0).  These are arrays with initial entries of 0
        self.x_values = [0]
        self.y_values = [0]

    # Exercise 15-5: Create new method called get_step() to determine direction
    # and distance for each step and calculate step
    def get_step(self):
        """Replace code from lengthy fill_walk() method"""
        # Exercise 15-4: change values in RandomWalk() to observe the change
        # in output
        direction = choice([1, -1])
        distance = choice([0,1,2,3,4,5,6,7,8])
        step = (direction * distance)
        return step

    def fill_walk(self):
        """Calculate all the points in a walk"""

        # Keep taking steps until the walk reaches num_points
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far.  Result is x_step.
            # x_direction is a binary choice so it's either -1 or 1
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere. 'continue' returns to begining of
            # while loop
            if x_step == 0 and y_step == 0:
                continue

            # Calculate next values of x and y. [-1] is an index denoting the last
            # value of an array.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # Append next x and y values to their respective arrays
            self.x_values.append(next_x)
            self.y_values.append(next_y)
