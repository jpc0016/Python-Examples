# CH6 Exercise 6-5: Rivers
#
# August 7, 2019
#
# dictionary of three rivers with their countries
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states'
}

# Loop to write a sentence about each river.
for river in rivers.keys():
    print("The " + river.title() + " River runs through " + rivers[river].title() + ".")


# Loop to print name of each river
print(" ")
for river in rivers.keys():
    print(river.title() + " River.")


# Loop to print name of each country in dictionary
print(" ")
for country in rivers.values():
    print(country.title())
