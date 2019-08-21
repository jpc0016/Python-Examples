# CH10 Exercise 10-1
#
# learning_python.py
#
# Open learning_python.txt and print its contents 3 times
filename = 'learning_python.txt'

# Print contents by reading entire file
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)
    file_object.close()

# Print contents by looping over file object
with open(filename) as f:
    lines = f.readlines()

    for line in lines:
        print(line.rstrip())

    f.close()

print(" ")

# Print contents by storing lines in a list and working with them outside the
# with block
with open(filename) as file_object:
    lines = file_object.readlines()

working_string = ''
for line in lines:
    working_string += line.rstrip()

print(working_string)
