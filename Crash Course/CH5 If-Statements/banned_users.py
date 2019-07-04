# CH5 example
#
# Check whether a value is not in a list with an if statement
#
# set list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
