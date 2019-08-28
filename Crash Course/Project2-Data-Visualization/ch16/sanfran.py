# CH16 Exercise 16-1
#
# sanfran.py
#
# Are temperatures in San Francisco more like temperatures in Sitka or in
# Death Valley?
# Generate high-low temperature plot for San Francisco using the source:
# http://www.wunderground.com/history/
# Use 2018 data
from csv import *
from datetime import datetime

try:
    import matplotlib.pyplot as plt
except (NameError, ImportError, ModuleNotFoundError) as e:
    print("Cannot import matplotlib for some reason.")
    quit(0)

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
