# CH16 Exercise 16-1
#
# death.py
#
# Are temperatures in San Francisco more like temperatures in Sitka or in
# Death Valley?
# Generate high-low temperature plot for San Francisco using the source:
# http://www.wunderground.com/history/
# cannot find San Francisco csv links so using Death Valley data
# Use 2018 data
import csv
from datetime import datetime

try:
    import matplotlib.pyplot as plt
except (NameError, ImportError, ModuleNotFoundError) as e:
    print('Cannot import matplotlib for some reason.')
    quit(0)

filename = 'data/death_valley_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Continue extracting DATE (row[2]), max temperature TMAX (row[6]), and
    # min temperature TMIN (row[7]).  Loop through each row in the csv file.
    # MAKE SURE LISTS ARE DECLARED OUTSIDE FOR LOOP
    dates = []
    highs = []
    lows = []

    for row in reader:

        try:
            date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[6])
            low = int(row[7])
        except ValueError:
            print(date, 'missing data')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)


    # print(lows)
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='red', alpha=0.1)

    fig.autofmt_xdate()
    plt.title('High and Low Temperatures - 2018\nDeath Valley, CA', fontsize=20)
    plt.xlabel('', fontsize=14)
    plt.ylabel('Temperature (F)', fontsize=14)

    plt.tick_params(axis='both',which='major',labelsize=14)

    plt.show()
