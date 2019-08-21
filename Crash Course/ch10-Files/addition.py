# CH10 Exercise 10-6
#
# addition.py
#
# prompt user for two numbers and handle an error if text is received.  Type is
# ValueError
print("Add two numbers together ")

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

try:
    # int() statements must be here since they are being checked by the try block
    sum = int(first_number) + int(second_number)
except ValueError:
    print("Both numbers must be strings.")
else:
    print("Sum is " + str(sum))
