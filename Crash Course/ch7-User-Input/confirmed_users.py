# CH7 Example
#
# confirmed_users.py
#
# Moving items from one list to another
#
# While loop to move users from unconfirmed list
# to confirmed list

# Start with users that need to be verified and an empty
# list to place them in
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Loop through unconfirmed_users list and pop each name
# Add each name to confirmed_users list
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user " + current_user.title() + "...")
    confirmed_users.append(current_user)

# Display confirmed_users
print("\nThe following users have been confirmed:  ")
for user in confirmed_users:
    print(user.title())
