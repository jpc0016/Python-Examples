# CH15 Example
#
# die_visual.py
#
# Introduction to Pygal
# Import die.py Die() class to analyze and plot die rolls
from die import Die
import pygal

# Create a D12 and D20 die
die_1 = Die(12)
die_2 = Die(20)

# Make some rolls
results = []
for roll_num in range(100000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze frequencies
# loop through each number from 1 to num_sides.  Loop will stop executing at die.num_sides
# so the range limit must be die.num_sides+1
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
label = []
for value in range(2, max_result+1):
    # .count() counts the number of times a value appears in a list
    frequency = results.count(value)
    frequencies.append(frequency)
    # x_labels can be generated with this simple line
    label.append(str(value))


# Create histogram using Pygal
hist = pygal.Bar()

# hist.title = "Results of rolling two D6 50000 times."
# Exercise 15-6: replace hist.x_labels to generate the labels automatically
hist.title = "Results of rolling one D12 and one D20 50,000 times."
hist.x_labels = label
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

# Open die_visual.svg in a web browser
hist.add('D12 + D20', frequencies)
hist.render_to_file('die_visual.svg')



# This prints the first 5 elements of results.  Similar to using a head() method
#print(results[:5])
print(frequencies)
