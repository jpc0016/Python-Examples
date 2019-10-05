# CH15 Exercise 15-10
#
# random_pygal.py
#
# Use pygal to vizualize a random walk.  Pygal is the visualization library that
# contains histograms and other plots
import pygal
from random_walk import RandomWalk

# Create new random walk with just 1000 points and run fill_walk() method
new_walk = RandomWalk(1000)
new_walk.fill_walk()


# Create list of tuples for xy_chart using a function and list comprehension
def merged(list1, list2):
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list

# Merge x and y lists from new_walk instance
points = merged(new_walk.x_values, new_walk.y_values)

# Correctly color first and last points of the merged list.  I can't believe how
# much work goes into this crap.  This is why we use matplotlib...
formatted_points = []
for item in points:
    if item == points[0]:
        formatted_points.append({"value": item, "color": "green"})
    elif item == points[-1]:
        formatted_points.append({"value": item, "color": "blue"})
    else:
        formatted_points.append(item)

# Initialize chart
xy_chart = pygal.XY(stroke=False)

# Set title and labels
xy_chart.title = "Random Walk Output"
xy_chart.add('Result', formatted_points)
# xy_chart.add('Start', {points[0]: 'green'})
# xy_chart.add('End', {points[-1]: 'blue'})
xy_chart.render_to_file("chart.svg")
