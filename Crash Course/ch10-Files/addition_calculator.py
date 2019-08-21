# CH10 Exercise 10-7
#
# addition_calculator.py
#
# wrap addition.py in a while loop

while True:
    print("\nAdd two numbers together ")

    first_number = input("Enter the first number: (Enter 'q' to quit)")
    if first_number.lower() == 'q':
        break

    second_number = input("Enter the second number: (Enter 'q' to quit)")
    if second_number.lower() == 'q':
        break

    try:
        # int() statements must be here since they are being checked by the try block
        sum = int(first_number) + int(second_number)
    except ValueError:
        print("Both numbers must be strings.")
    else:
        print("Sum is " + str(sum))
