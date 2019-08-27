# CH15 Exercise 15-7
#
# two_die.py
#
# Simulate running two 8-sided die 1,000 times.  Increase the number of rolls
# until a limit is reached.  9 is consistent max result.
from die import Die
import pygal

# Create two D8 die
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze frequencies
# loop through each number from 1 to max_result of sides.  Loop will stop
# executing at die.num_sides so the range limit must be die.num_sides+1
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

# hist.title = "Results of rolling two D8 1,000 times."
hist.title = "Results of rolling two D8 1,000 times."
hist.x_labels = label
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D8 + D8', frequencies)
hist.render_to_file('two_die.svg')



# This prints the first 5 elements of results.  Similar to using a head() method
#print(results[:5])
print(frequencies)
