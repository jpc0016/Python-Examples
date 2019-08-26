# CH15 Example
#
# mpl_squares.py
#
# Plotting a simple line graph using matplotlib
# The following does not work on Python3 idk why
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Cannot import pyplot for some reason.")

# Initialize input array
input_values = [1,2,3,4,5]

# Initialize output array
squares = [1,4,9,16,25]

# Create plot
plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()
