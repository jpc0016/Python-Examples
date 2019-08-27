# CH15 Exercise 15-10
#
# matplotdie.py
#
# Use matplotlib to make a die-rolling vizualization.  Use Python2.7
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Cannot import pyplot for some reason.")

from die import Die

die = Die()

# Create array of raw roll results
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Count number of times an outcome appears in results[] and store in
# frequencies[].  Also create label for plt.plot
frequencies = []
x_values = []
for number in range(1, die.num_sides+1):
    frequency = results.count(number)
    frequencies.append(frequency)
    x_values.append(str(number))

# Create plot with x_values[] and frequencies[]
plt.bar(x_values, frequencies)

# Set title and axes labels
plt.title("Result of rolling D6 1,000 times.", fontsize=24)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)

plt.show()
