# Chapter 3 Exercises 3-4, 3-5, and 3-6
#
# Create a guest list of people to invite to dinner and
# change it according to instructions.

# Exercise 3-4
# Initial guest list
guests = ['Claire', 'Obama', 'Kid Rock', 'Bill Burr']

# Iterate over list to print personal invitation

# Below is a basic for-loop that solves the exercise
# i = 0
# for item in guests:
#    print("Hello " + guests[i] + "!")
#    i += 1

# Below is list comprehension for-loop.  It has the same
# output as the above basic loop
# Note:
j = 0
[print("Good evening " + guests[j] + ", you have been invited the first ever dinner with JohnGuy01!!") for j in range(len(guests))]

# Exercise 3-5
# A guest cannot make it to dinner!
print("\nUnfortunately former President Obama is unable to make it to dinner!  :(")

# Modify your list, replacing Obama with
# the name of the new person you are inviting.
guests.remove('Obama')
guests.append('Randy Marsh')
print("")
print("The new list is below:")
print(guests)
print("")

# Print second set of invitations to include Randy
k = 0
[print("Pardon the interuption, " + guests[k] + ", you are receiving a new invitation for dinner with JohnGuy01!") for k in range(len(guests))]
print("")

# Exercise 3-6
# Add three more guests to invite to dinner
#   Add one to beginning
#   Add one to middle of list
#   Add one to end of list
guests.insert(0, 'Ghengis Khan')
guests.insert(int(len(guests)/2), 'Bison Dison')
guests.append('Josh Lospinoso')

# Print new invitation messages about finding a bigger table
m = 0
[print("Fantastic news, " + guests[m] + ", we found a bigger table!  Attached is your latest invitation!") for m in range(len(guests))]
