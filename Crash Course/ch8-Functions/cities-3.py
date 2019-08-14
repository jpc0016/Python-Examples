# CH8 Exercise 8-5 and 8-6
#
# cities-3.py
#
# Write a function called describe_city() with parameters, city, and country
# Print a simple sentance of the city and country.

# Exercise 8-5
def describe_city(city, country='brazil'):
    print(city.title() + " is in " + country.title() + ".")

describe_city('hamburg', 'germany')

describe_city('beijing')
describe_city('berlin')
describe_city('warsaw')


# Exercise 8-6
# Write a function called city_country() with parameters, city, and country
# Return formatted string like this: "Seattle, United States"
def city_country(city, country):
    print(city.title() + ", " + country.title() + ".")

city_country('madrid', 'spain')
city_country('cairo', 'egypt')
city_country('taipei', 'taiwan')
