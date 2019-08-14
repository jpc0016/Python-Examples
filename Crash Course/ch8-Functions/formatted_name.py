# CH8 Example
#
# formatted_name.py
#
# Return Values in Functions.
#
# Function that takes a first and last name and outputs a formatted full name
# Note: middle_name is an optional parameter.  This only works if placed at the end
# of the parameter list
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name neatly formatted"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# Output: 'Jimi Hendrix'

# middle_name must be the last parameter passed
assassin = get_formatted_name('john',  'booth', 'wilkes')
print(assassin)
# Output: 'John Wilkes Booth'
