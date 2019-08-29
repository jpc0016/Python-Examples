# CH16 Exercise 16-3
#
# rain.py
#
# Plot rainfall of Death Valley, California
import csv
from datetime import datetime

# Attempt to import matplotlib
try:
    import matplotlib.pyplot as plt
except (ValueError, ImportError, ModuleNotFoundError) as e:
    print("Cannot import matplotlib for some reason.")
    print("Exit code 0")
    quit(0)

# Open csv file as filename
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Check header_row for correct columns
    # print(header_row)

    # Initialize the columns of interest as empty arrays
    precipitation = []
    dates = []

    # Iterate over each row in the csv file
    for row in reader:
        try:
            date = datetime.strptime(row[2], '%Y-%m-%d')
            prcp = float(row[3])
            print(prcp)
        # Make statement if data value is not present
        except ValueError:
            print(date, "missing data")
        else:
            dates.append(date)
            precipitation.append(prcp)

    #print(dates)
    # Create plot
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, precipitation, c='blue')
    fig.autofmt_xdate()

    # Create plot labels and tick marks
    plt.title("Yearly Precipitation in Death Valley, CA - 2018", fontsize=20)
    plt.xlabel('', fontsize=16)
    plt.ylabel('Rainfall', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    # Show plot
    plt.show()
