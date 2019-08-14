# CH8 Exercise 8-3
#
# shirt.py
#
# Write a function called make_shirt() with parameters, size, and message
# to print on shirt.  Print a sentance summarizing the shirt size and message.
def make_shirt(shirt_size, message='hello'):
    shirt_size = shirt_size.upper()

    # Check for sizes
    if shirt_size == 'M':
        print("\nT-shirt size: " + shirt_size)
    elif shirt_size == 'S':
        print("\nT-shirt size: " + shirt_size)
    elif shirt_size == 'L':
        print("\nT-shirt size: " + shirt_size)
    else:
        print("\nSorry, we don't carry that size!")
    

    # Print message
    print("T-shirt message: " + message)

# Prompt user for input
size = input("\nWhat is your T-shirt size? (S/M/L)  ")
message = input("\nType a message for your T-shirt.  ")

# Explicitly provides message
make_shirt(size, message)

# Uses default message
make_shirt(size)
