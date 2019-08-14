# CH6 Exercise 6-3
#
# Glossary of terms
# July 29, 2019
#
# Use 5 programming words as dictionary keys and their definitions as values.  Print each word and its meaning.

glossary = {'foo': 'bar', 'air': 'borne', 'blue': 'falcon', 'fizz': 'buzz', 'war': 'eagle'}

for item in glossary:
    print(item + ": " + glossary[item])
