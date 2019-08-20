# CH10 Example
#
# pi_string.py
#
# Working with a file's contents
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print("PI Length: " + str(len(pi_string)))
