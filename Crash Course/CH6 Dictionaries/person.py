# CH6 Exercise 6-1
#
# person.py
#
# Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live.

guy = {
    'first_name': 'buddy',
    'last_name': 'pal',
    'age': 40,
    'city': 'San Francisco'
    }

# Dictionary print is not in order.  'city' value prints first.
for item in guy:
    #print(item)
    print(guy[item])

# print("")
# print(guy['first_name'])
# print(guy['last_name'])
# print(guy['age'])
# print(guy['city'])
