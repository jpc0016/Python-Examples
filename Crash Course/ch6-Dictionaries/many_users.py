# CH6 Example
#
# many_users.py
#
# Dictionary within a dictionary
#
# Create dictionary of users including first name, last name, location
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

# user_info contains the contents of each user in the secondary braces {}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())
