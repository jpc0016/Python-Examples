# CH16 Exercise 16-2
#
# two_graphs.py
#
# Plotting high and low temperatures of both Sitka, Alaska and Death Valley,
# California
import csv
from datetime import datetime

# Attempt to import matplotlib
try:
    import matplotlib.pyplot as plt
except (NameError, ImportError, ModuleNotFoundError) as e:
    print("Cannot import matplotlib for some reason...")
    quit(0)

# Import Sitka dataset
filename = 'data/sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from file.  TMAX is at index 5 in
    # sitka_weather_07-2018_simple.csv. Loop through each row in reader
    # object AFTER the header_row
    dates, highs, lows = [], [], []

    for row in reader:
        # convert each element into an integer before storing into the list.
        # This is to prepare data for matplotlib
        try:
            date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[8])
            low = int(row[9])
        except ValueError:
            print(date, 'missing data')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

    # Import Death Valley dataset while sitka dataset is open
    item = 'data/death_valley_2018_full.csv'
    with open(item) as file_object:
        reader_object = csv.reader(file_object)
        header= next(reader_object)

        # Continue extracting DATE (row[2]), max temperature TMAX (row[6]), and
        # min temperature TMIN (row[7]).  Loop through each row in the csv file.
        # MAKE SURE LISTS ARE DECLARED OUTSIDE FOR LOOP
        dv_dates = []
        dv_highs = []
        dv_lows = []

        for data in reader_object:

            try:
                dv_date = datetime.strptime(data[2], '%Y-%m-%d')
                dv_high = int(data[6])
                dv_low = int(data[7])
            except ValueError:
                print(dv_date, 'missing data')
            else:
                dv_dates.append(dv_date)
                dv_highs.append(dv_high)
                dv_lows.append(dv_low)



    #print(dates)

    # Plot Sitka points
    fig = plt.figure(dpi=128, figsize=(12, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)

    # Plot Death Valley points
    plt.plot(dv_dates, dv_highs, c='red', alpha=0.5)
    plt.plot(dv_dates, dv_lows, c='blue', alpha=0.5)


    # fill between both lines.  'alpha' controls opacity
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor='red', alpha=0.1)

    # Format plot
    plt.title('Daily High and Low Temperatures - 2018\nSitka, AK and Death' +
    ' Valley, CA', fontsize=18)
    plt.xlabel('', fontsize=14)
    # Auto-format dates
    fig.autofmt_xdate()
    plt.ylabel('temperature (F)', fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)

    plt.show()

    # enumerate() returns an index of each item in header_row.  Very handy
    # in creating numbered lists.
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
