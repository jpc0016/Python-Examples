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
else:
    squares = [1,4,9,16,25]
    plt.plot(squares)
    plt.show()
