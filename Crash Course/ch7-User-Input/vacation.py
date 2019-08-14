# CH7 Exercise 7-10
#
# vacation.py
#
# Poll users about a dream vacation
# Print the result of the poll

# Create poll status variable to use with while loop
poll_status = True

# Create empty dictionary to hold answers
vacations = {}

while poll_status:

    name = input("What is your name?  ")
    vacation = input("If you could visit one place in the world, where would you go?  ")

    # Update dictionary with name and vacation
    vacations[name] = vacation

    # Continue polling?
    keep_polling = input("Add more members?  (y/n)  ")
    if keep_polling == 'n' or keep_polling == 'N':
        poll_status = False

# Print results of poll
print(" ")
for name, vacation in vacations.items():
    print(name.title() + " would like to visit " + vacation.title() + " someday!")
