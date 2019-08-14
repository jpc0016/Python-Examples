# CH8 Example
#
# greet_users.py
#
# Passing lists to functions.
# Start with simple greeter function from greeter.py
def greet_users(names):
    """Pring a simple greeting to each user"""
    for name in names:
        print("Hello, " + name.title() + "!")

# Set list of names and pass into greet_users()
usernames = ['dwight', 'danesh', 'gilfoyle']
greet_users(usernames)
