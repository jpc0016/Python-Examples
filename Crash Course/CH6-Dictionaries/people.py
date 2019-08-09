# CH6 Exercise 6-7
#
# people.py
#
# Starting with person.py, create 2 new dictionaries and store all three entries into a
# dictionary called 'people'.  Loop through list to print each person's attributes

# Troubleshoot note: the entry names (guy, jeff, ahmed) need to be in quotes ''
people = {
    'guy': {
        'first_name': 'buddy',
        'last_name': 'pal',
        'age': 40,
        'city': 'san francisco',
        },

    'jeff': {
        'first_name': 'jeff',
        'last_name': 'foxworthy',
        'age': 30,
        'city': 'new  york city',
        },

    'ahmed': {
        'first_name': 'ahmed',
        'last_name': 'islamabad',
        'age': 27,
        'city': 'flint',
        },
      }


# Dictionary print is not in order.  'city' value prints first.
for person, attributes in people.items():
    print("\nEntry: " + person)
    full_name = attributes['first_name'] + " " + attributes['last_name']
    age = attributes['age']
    city = attributes['city']

    # print attributes of each person
    print("\tFull name: " + full_name)
    print("\tAge: " + str(age))
    print("\tCity: " + city)


# print("")
# print(guy['first_name'])
# print(guy['last_name'])
# print(guy['age'])
# print(guy['city'])
