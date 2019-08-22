# CH11 Exercise 11-1 and 11-2
#
# city_functions.py
#
# Write a function that accepts city name and a country name and return a string
# of the form 'City, Country'

# Exercise 11-2: modify function to require population as a third parameter
def city_country(city, country, population=''):
    """Neatly format a city and country into a proper string"""
    # Form is now 'City, Country - population $population'
    if population:
        formatted_string = city.title() + ", " + country.title() + " - population " + str(population)
    else:
        formatted_string = city.title() + ", " + country.title()
    return formatted_string
