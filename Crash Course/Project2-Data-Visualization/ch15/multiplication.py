# CH15 Exercise 15-9
#
# multiplication.py
#
# Simulate multiplying the resutls of D6 rolls.
from die import Die
import pygal

# Create two D6 die
die_1 = Die()
die_2 = Die()

# Make some rolls
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze frequencies
# loop through each number from 1 to max_result of sides.  Loop will stop
# executing at die.num_sides so the range limit must be die.num_sides+1
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
label = []
for value in range(1, max_result+1):
    # .count() counts the number of times a value appears in a list
    frequency = results.count(value)
    frequencies.append(frequency)
    # x_labels can be generated with this simple line
    label.append(str(value))


# Create histogram using Pygal
hist = pygal.Bar()

hist.title = "Results of multiplying two D6 1,000 times."
hist.x_labels = label
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 * D6', frequencies)
hist.render_to_file('multiplication.svg')
# Certain numbers in the range of 1 to 36 have factors not present on 6-sided die.
# Many of these numbers are also prime


# This prints the first 5 elements of results.  Similar to using a head() method
#print(results[:5])
print(frequencies)
