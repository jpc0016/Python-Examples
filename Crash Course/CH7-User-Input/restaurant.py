# CH7 Exercise 7-2
#
# restaurant.py
#
# Ask user how many people are in their restaurant party
# If the party is more than 8, print that they have to wait
party_number = input("How many guests?  ")


if int(party_number) > 8:
    print("\nYou will have to wait for a table.")
else:
    print("\nYour table is ready.  Right this way!")
