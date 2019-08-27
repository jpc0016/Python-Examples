# CH16 Example
#
# high_lows.py
#
# Parsing CSV files
# Plotting high and low temperatures of Sitka, Alaska in 2018
import csv
from datetime import datetime

# Run in Python2.7 until matplotlib is fixed for Python3.7
try:
    import matplotlib.pyplot as plt
except:
    print("Cannot import matplotlib for some reason...")

# Use full dataset once testing complete on sample set
filename = 'data/sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from file.  TMAX is at index 5 in
    # sitka_weather_07-2018_simple.csv. Loop through each row in reader
    # object AFTER the header_row
    dates, highs, lows = [], [], []

    for row in reader:
        # convert each element into an integer before storing into the list. This is
        # to prepare data for matplotlib
        try:
            high = int(row[8])
            low = int(row[9])
        except:
            high = 0
            low = 0
        highs.append(high)
        lows.append(low)

        date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(date)

    #print(highs)

    # Plot data points in a temperature chart (normal line chart)
    # plt.figure() customizes the plot figure instead of using default plt.plot values
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    # fill between both lines.  'alpha' controls opacity
    plt.fill_between(dates, highs, lows, facecolor='red', alpha=0.1)

    # Format plot
    plt.title("Daily High and Low Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    # Auto-format dates
    fig.autofmt_xdate()
    plt.ylabel("temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

    # enumerate() returns an index of each item in header_row.  Very handy in
    # creating numbered lists.
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
