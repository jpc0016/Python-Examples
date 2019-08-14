# CH7 Exercise 7-5
#
# movie-tickets.py
#
# If a person is under 3 years old, ticket is free
# If person is between 3 and 12, ticket is $10
# Ticket is $15 if over 12
#
# Write loop to prompt user for age and tell them movie ticket cost

prompt = "\nWhat is your age?  "
prompt += "\nType 'quit' to exit.  "

while True:
    age = input(prompt)
    if age == 'quit':
        break

    if int(age) < 3:
        print("Your ticket is free!")
        continue
    elif int(age) <= 3 and int(age) <= 12:
        print("Your ticket is $10.")
        continue
    else:
        print("Your ticket is $15.")
        continue
