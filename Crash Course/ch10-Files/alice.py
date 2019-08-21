# CH10 Example
#
# alice.py
#
# Handling FileNotFoundError Exception
# attempt to read contents of Alice in Wonderland but no alice.txt file
# exists

filename = 'alice.txt'

try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # Count approximate words in the book.  Use split() method to make each word
    # its own entry in an array 'words'
    words = contents.split()
    num_words = len(words)
    print("The book " + filename + " has approximately " + str(num_words) + " words.")
