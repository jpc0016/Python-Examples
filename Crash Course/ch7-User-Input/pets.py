# CH7 Example
#
# pets.py
#
# Removing instances of a specific value
# from a list

# Run while loop until all instances of 'cat' are no longer in list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

# 'cat' is removed
print(pets)
