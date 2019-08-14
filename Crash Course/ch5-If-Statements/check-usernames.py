# CH5 Exercise 5-10
#
# Check usernames
# Create a program that ensures everyone has a unique username.
#
# Create list of five or more usernames
current_users = ['Jeff', 'Tina', 'admin', 'Jerome', 'Danesh', 'Erlich']

# Create another list of five users with one name from current_users
new_users = ['Jared', 'danesh', 'Collin', 'jeff', 'Yang']

# Loop through new_users to see if a username has been used in current_users.
# comparison must not be case sensitive
for user in new_users:
    if user.title() in current_users:
        print("Please enter a new username.")
    else:
        print(user + " is available.")
