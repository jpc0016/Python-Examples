# CH10 Exercise 10-2
#
# replacing.py
#
# Open learning_python.txt and replace any word in the file with a different
# string
filename = 'learning_python.txt'

with open(filename) as file_object:

    contents = file_object.read()
    # contents.replace() does not automatically replace contents.  Must assign the
    # replacement to another value such as new_line or do print(contents.replace())
    new_line = contents.replace('text file', 'TEXT FILE I WROTE')
    print(new_line)
