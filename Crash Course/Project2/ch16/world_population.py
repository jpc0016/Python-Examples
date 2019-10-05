# CH16 Example
#
# world_population.py
#
# Parsing JSON files
# Analyzing global population
#
# Dependencies specific to this script:
# > sudo pip3 install pygal
# > sudo pip3 install pygal_maps_world
import json
from country_code import get_country_code
import pygal

# Load data into a list
filename = 'data/global_population.json'
with open(filename) as f:
    pop_data = json.load(f)
    # print(pop_data)

# Continue world population example (page 369-370)
# Build a dictionary of population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict["Year"] == 1990.0:
        average = pop_dict['Average']
        biraben = pop_dict['Biraben']
        # --snip--
        # Repeat for each dictionary variable in the JSON file

        print("Average world population in " + str(pop_dict['Year']) + ": "
        + str(average) + " million")

# print(average)
# print(biraben)
