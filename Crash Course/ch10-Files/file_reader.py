# CH10 Example
#
# file_reader.py
#
# Reading an entire file and printing its contents
# open() returns a file object representation of pi_digits.txt and stores it
# into f.  The parameter in open() is a file path.
with open('pi_digits.txt') as f:
    contents = f.read()
    # .rstrip() removes white space from the right side of the string
    print(contents.rstrip())
    f.close()

print(" ")

filename = 'pi_digits.txt'
# this loop reads line by line
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
    file_object.close()

print(" ")

# This loop allows access to file contents outside the 'with' statement by storing
# contents as lines
with open(filename) as file_object:
    lines = file_object.readlines()

# print the lines
for line in lines:
    print(line.rstrip())
