# CH10 Example
#
# divide.py
#
# Exception Handling
# attempt to divide by zero and handle it with try-except blocks

print("Give me two numbers and I'll divide them.")
print("Enter 'q' to stop.")

while True:
    first_number = input("\nEnter first number: ")
    if first_number.lower() == 'q':
        break

    next_number = input("\nEnter second number: ")
    if next_number.lower() == 'q':
        break

    try:
        # error occurs on this line
        answer = int(first_number)/int(next_number)
    except ZeroDivisionError:
        print("Can't divide by zero!")
    else:
        print(str(answer))
