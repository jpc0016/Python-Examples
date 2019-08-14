# CH8 Exercise 8-13
#
# user_profile-2.py
#
# Start with user_profile.py
# Create your own profile with first and last names and three other key-value pairs
def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything about
    a user
    """
    profile = {}

    # These items are statically provided
    profile['first_name'] = first
    profile['last_name'] = last

    # Loop through remainin parameters provided to user_info
    for key, value in user_info.items():
        profile[key] = value
    return profile

# 'albert' and 'einstein' are first and last respectively.  The remaining items,
# location and field, are items in the dictionary user_info
user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics'
                            )
print(user_profile)

my_profile = build_profile('John', 'Guy',
                            location='earth',
                            field='science',
                            species='human'
                            )
print(my_profile)
