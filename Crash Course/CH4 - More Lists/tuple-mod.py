# CH4 Writing Over a Tuple
#
# Although you can’t modify a tuple, you can assign a new value to a variable
# that holds a tuple.

# define original tuple
dimensions = (200, 50)

print("Original dimensions:")
for item in dimensions:
    print(item)

# define new tuple to overwrite original tuple
dimensions = (400, 100)

print("\nUpdated dimensions:")
for dimension in dimensions:
    print(dimension)
