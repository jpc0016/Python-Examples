# CH6 Exercise 6-9
#
# favorite_places.py
#
# Dictionary within a dictionary exercise
# Create a dictionary of names and store 1 - 3 favorite places per person

places = {
    'matt':['ohio', 'new zealand', 'miami'],
    'luke': ['jerusalem'],
    'jin': ['hong kong', 'beijing', 'los angeles'],
    'danny': [],
}

# Loop through each person and list in the dictionary
for name, locations in places.items():
    print("\nHey " + name.title() + ", what are your favorite places?" )
    if len(locations) == 0:
        print("\tI hate traveling.")
    elif len(locations) == 1:
        print("\tMy favorite place is " + locations[0].title())
    else:
        print("\tMy favorite places are:")
        # Run another for-loop to handle multiple favorite places
        for place in locations:
            print("\t" + place.title())
