# CH11 Example
#
# names.py
#
# Test function in name_function.py
from name_function import get_formatted_name

print("Press 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first.lower() == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if last.lower() == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")
