# CH10 Exercise 10-3
#
# guest.py
#
# Prompt user for their name and add it to guest.txt
filename = 'guest.txt'

with open(filename, 'w') as f:
    name = input("What is your name? ")
    f.write(name.title() + "\n")
