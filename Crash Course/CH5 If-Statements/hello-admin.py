# CH5 Exercise 5-8 and 5-9
#
# Hello Admin
#
# Make a list of 5+ usernames including 'admin' and print a greeting to each
# user
# Populate username list
users = ['Jeff', 'Tina', 'admin', 'Jerome', 'Danesh', 'Erlich']
#users = []

# Add if test to ensure list is not empty
if users:
    for user in users:
    # The below commented code could be insecure
    #if user.lower() == 'admin':
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again.")
else:
    print("We need to find some users!")
