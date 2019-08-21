# CH10 Exercise 10-10
#
# common_words.py
#
# Using texts from gutenberg.org use count() to find the number of times a word
# appears in a string

def find_words(filename, word):
    """
    Function to find the number of times 'word'
    appears in a file, filename
    """
    with open(filename) as f:
        contents = f.read()
        total = contents.lower().count(word)
        print(total)


find_words('alice.txt', 'clark')
