# CH6 Exercise 6-11
#
# cities.py
#
# Make a dictionary called cities.
# Create a dictionary of information about three cities to include country, population,
# and a fact.  Print the name of each city and their attributes

# Define the cities dictionary
cities = {
    'huntsville': {
        'country': 'us',
        'population': 194000,
        'fact': 'found in 1812',
    },

    'las vegas': {
        'country': 'us',
        'population': 642000,
        'fact': 'location of BH and DC',
    },

    'madrid': {
        'country': 'spain',
        'population': 3174000,
        'fact': 'capital of Spain',
    },
}

# Print each city and their attributes
for city, attributes in cities.items():
    print("\nCity: " + city.title())
    # Loop through each sub-dictionary's attributes and print them
    for item in attributes:
        print("\t" + item.title() + ": " + str(attributes[item]))
