# CH8 Example
#
# pets-2.py
#
# Positional Arguments:
# Parameter values are matched up in the order provided

# Function to describe a pet
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Order matters when calling a function because that is how the function definition
# reads.  Reversing the parameter values will produce weird strings.
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


# Keyword Arguments
# Assign the parameters during the function call.  Order does not matter here.
describe_pet(pet_name='socks', animal_type='cat')

# Can define default values in the function definition.
# Change order of parameters because Python interprets default values as positional arguments
def describe_dog(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_dog(pet_name='jeff')

# Python will use animal_type below since it is explicitly provided
# The default value in function definition will be overwritten.
describe_dog(pet_name='toby', animal_type='cat')
