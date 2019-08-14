# CH6 Exercise 6-8
#
# pets.py
#
# Create several dictionaries of pets and store them in a list called 'pets'
# Loop through list to print each pet's attributes

pets = {
    'maru': {
        'name': 'maru',
        'species': 'cat',
        'age': 6,
        'owner': 'clr',
    },

    'boots': {
        'name': 'boots',
        'species': 'cat',
        'age': 4,
        'owner': 'jhn',
    },

    'jake': {
        'name': 'jake',
        'species': 'dog',
        'age': 3,
        'owner': 'clr',
    },

    'socks': {
        'name': 'socks',
        'species': 'cat',
        'age': 1,
        'owner': 'jhn',
    },
}

for name, attributes in pets.items():
    print("\nPet: " + name.title())
    print("\tName: " + attributes['name'].title())
    print("\tSpecies: " + attributes['species'].title())
    print("\tAge: " + str(attributes['age']))
    print("\tOwner: " + attributes['owner'].title())
