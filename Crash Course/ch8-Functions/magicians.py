# CH8 Exercise 8-9, 8-10, and 8-11
#
# magicians.py
#
# Exercise 8-9
# Pass a list of magicians to a function, show_magicians(), which prints
# the name of each magician
def show_magicians(magician_list):
    """Print each magician"""
    for name in magician_list:
        print(name.title())

# Declare magicians list
magicians = ['jared', 'john edward', 'george']
show_magicians(magicians)


# Exercise 8-10
# Write function called make_great() that modifies the list by adding "the Great"
# to each name
def make_great(magician_list):
    """Add 'the Great' to each name"""
    great_list = []

    for magician in magician_list:
        magician = magician.title() + " the Great"
        great_list.append(magician)

    return great_list

print(" ")
great_magicians = make_great(magicians)
show_magicians(great_magicians)

# Exercise 8-11
# Show that original list, magicians, was not changed.
print(" ")
show_magicians(magicians)
