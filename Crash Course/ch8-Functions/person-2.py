# CH8 Example
#
# person-2.py
#
# Returning a dictionary from a function
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {
        'first': first_name,
        'last': last_name,
            }

    # Check if age is entered
    if age:
        person['age'] = age
    return person


dead = build_person('jeffrey', 'epstein', age=64)
print(dead)
