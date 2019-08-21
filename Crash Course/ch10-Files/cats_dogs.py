# CH10 Exercise 10-8 and 10-9
#
# cats_dogs.py
#
# Make text files cats.txt and dogs.txt. Write program that reads contents of these
# files and prints to screen. Use FileNotFoundError for the except block.
# For 10-9 use 'pass' to make program fail silently

# Create function with try-except block to display contents of a file.
def display_contents(filename):
    """Show contents of a file given its presence"""

    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        #print("\nFile " + filename + " not found!\n")
        pass

# Call function with list of files
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    display_contents(filename)
