# CH10 Exercise 10-5
#
# reason.py
#
# Programming Poll
# Write while loop prompting user why they like programming.  Record
# their reason in a file called reason.txt

filename = 'reason.txt'

with open(filename, 'w') as f:

    flag = True
    while flag:
        reason = input("\nWhy do you like programming? (Enter 'q' to stop) ")
        if reason.lower() == 'q':
            flag = False
        else:
            f.write(reason + "\n")

    f.close()
