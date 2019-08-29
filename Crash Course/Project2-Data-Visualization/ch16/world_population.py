# CH16 Example
#
# world_population.py
#
# Parsing JSON files
# Analyzing global population
import json

# Load data into a list
filename = 'data/global_population.json'
with open(filename) as f:
    pop_data = json.load(f)
    # print(pop_data)

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
