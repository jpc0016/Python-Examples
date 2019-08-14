# CH8 Example
#
# user_profile.py
#
# Using arbitrary keyword arguments.
#

# Use ** when you don't know ahead of time what kind of information will be
# passed to the function.  ** tells Python to create an empty dictionary for
# additional parameters to fill in
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
