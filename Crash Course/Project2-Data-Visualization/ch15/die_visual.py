# CH15 Example
#
# die_visual.py
#
# Introduction to Pygal
# Import die.py Die() class to analyze and plot die rolls
from die import Die
import pygal

# Create a D6
die = Die()

# Make some rolls
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze frequencies
# loop through each number from 1 to 6.  Loop will stop executing at die.num_sides
# so the range limit must be die.num_sides+1
frequencies = []
for value in range(1, die.num_sides+1):
    # .count() counts the number of times a value appears in a list
    frequency = results.count(value)
    frequencies.append(frequency)


# Create histogram using Pygal
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

# Open die_visual.svg in a web browser
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')



# This prints the first 5 elements of results.  Similar to using a head() method
#print(results[:5])
print(frequencies)
