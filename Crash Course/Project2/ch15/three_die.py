# CH15 Exercise 15-8
#
# three_die.py
#
# Simulate running three D6.
from die import Die
import pygal

# Create three D6 die
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze frequencies
# loop through each number from 1 to max_result of sides.  Loop will stop
# executing at die.num_sides so the range limit must be die.num_sides+1
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
label = []
for value in range(3, max_result+1):
    # .count() counts the number of times a value appears in a list
    frequency = results.count(value)
    frequencies.append(frequency)
    # x_labels can be generated with this simple line
    label.append(str(value))


# Create histogram using Pygal
hist = pygal.Bar()

# hist.title = "Results of rolling three D6 1,000 times."
hist.title = "Results of rolling three D6 1,000 times."
hist.x_labels = label
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6+D6+D6', frequencies)
hist.render_to_file('three_die.svg')



# This prints the first 5 elements of results.  Similar to using a head() method
#print(results[:5])
print(frequencies)
