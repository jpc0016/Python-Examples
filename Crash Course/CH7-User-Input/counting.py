# CH7 Example
#
# counting.py
#
# While loop introduction
# Use while loop to count through numbers 0 to 10
current_number = 0
while current_number < 10:
    current_number += 1

    # Introduction to 'continue'
    # 'continue' statement returns to the beginning of the loop based
    # on a conditional test
    if current_number % 2 == 0:
        continue

    print(current_number)

# Result is:
# 1
# 3
# 5
# 7
# 9
