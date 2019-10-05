# CH15 Exercise 15-1 and 15-2
#
# cubes.py
#
# Plot first five cubic numbers.  Then plot first 5000 cubic numbers.

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Cannot import pyplot for some reason.")

# Define input arrays
x_values = range(1,5000)
y_values = []
for x in x_values:
    y_values.append(x**3)

# Create plot
# Note: colormap is only available with plt.scatter() method
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', linewidth=4)

# Create Title and axes labels
plt.title('Cube of Numbers (x^3)', fontsize=24)
plt.xlabel('Input Values', fontsize=14)
plt.ylabel('Output', fontsize=14)

# Set range for each axis
plt.axis([1,5000,1,5000**3])

# Set tick size for both axes.
plt.tick_params(axis='both', labelsize=14)

plt.show()
