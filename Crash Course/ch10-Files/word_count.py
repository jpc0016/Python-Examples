# CH10 Example
#
# word_count.py
#
# moved contents of alice.py into its own function: count_words()
#

def count_words(filename):
    """Count approximate words of a title"""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
        # replace above 2 lines with 'pass' to make program fail silently.  No
        # traceback or error message is produced
        pass
    else:
        # Count approximate words in the book.  Use split() method to make each word
        # its own entry in an array 'words'
        words = contents.split()
        num_words = len(words)
        print("The book " + filename + " has approximately " + str(num_words) + " words.")

# Need to save the remaining books for all word counts to display
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
# Results:
    # The book alice.txt has approximately 17842 words.
    # Sorry, the file siddhartha.txt does not exist.
    # Sorry, the file moby_dick.txt does not exist.
    # Sorry, the file little_women.txt does not exist.
