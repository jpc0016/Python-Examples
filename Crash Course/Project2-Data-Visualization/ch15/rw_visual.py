# CH15 Example
#
# rw_visual.py
#
# Run the random_walk class to plot its points.  Run in Python2.7 until matplotlib
# is fixed for Python3
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Cannot import pyplot for some reason.")

from random_walk import RandomWalk

# Make a random walk and plot its points.  Wrap in while loop to continue making
# walks
while True:
    # Can add plot points to walk
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Create scatterplot with random_walk x and y value arrays. Use colormap to
    # show which points were plotted first.  Remove black outline as well
    values = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=values, cmap=plt.cm.Blues, edgecolor='none', s=1)

    # Can plot first and last values of the walk to see where the walk begins
    # and ends.  Make these points much larger (size 100)
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # Remove axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # Set the size of the output window
    plt.figure(figsize=(10,6))
    
    plt.show()

    # Must use raw_input() if using Python2.7
    keep_running = raw_input("Create another walk? (y/n)  ")
    if keep_running.lower() == 'n':
        break
