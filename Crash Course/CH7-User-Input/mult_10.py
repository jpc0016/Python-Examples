# CH7 Exercise 7-3
#
# mult_10.py
#
# Ask user for a number
# return if number is a multiple of 10

number = input("What is the number?  ")
number = int(number)  # convert to integer from string

# Check for modularity
if number % 10 == 0:
    # Also convert number back to string!
    print("\n" + str(number) + " is a multiple of 10.")
else:
    print("\n" + str(number) + " is not divisible by 10.")
