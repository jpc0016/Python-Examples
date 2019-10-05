# CH15 Example
#
# scatter_squares.py
#
# Plotting a simple scatter plot using matplotlib
# The following does not work on Python3 idk why
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Cannot import pyplot for some reason.")

# Set arrays of values
# Use a loop to set both arrays
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

# 's' sets the size of the dots
# 'edgecolor' eliminates black outlines around the data points
# 'c' sets color as a literal or as an RGB point between 0 and 1
# plt.scatter(x_values,y_values, c=(0,0.8,0.6), edgecolor='none', s=40)

# 'cm' assigns darker colors to higher values. List of y values are passed into 'c'
plt.scatter(x_values,y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set the range for each axis
plt.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Show plot
# plt.show()

# Can save plot to a file with the below command.  Second argument trims extra 
# white space around the plot
plt.savefig('squares_plot.png', bbox_inches='tight')
