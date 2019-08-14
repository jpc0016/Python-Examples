# CH7 Example
#
# mountain_poll.py
#
# Filling a dictionary with user input
#
responses = {}

# Set flag to indicate polling is active
polling_active = True

while polling_active:

    # Ask for user input
    name = input("\nWhat is your name?  ")
    response = input("What mountain would you like to climb some day?  ")

    # Store responses in the dictionary
    responses[name] = response

    # Ask if anyone else is taking the poll
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False


# Polling is complete.  Show results.
print("\n---Poll Results---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")
