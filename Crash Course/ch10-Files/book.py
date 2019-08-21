# CH10 Exercise 10-4
#
# book.py
#
# Write while loop prompting user for their name and printing a greeting.  Record
# their visit in a file called guest_book.txt

filename = 'guest_book.txt'

with open(filename, 'w') as f:

    flag = True
    while flag:
        name = input("\nWelcome!  What is your name? (Enter 'q' to quit)")

        if name.lower() == 'q':
            flag = False
        else:
            print(name.title() + ", please sign in!")
            f.write(name + "\n")
