# CH6 Exercise 6-4: Glossary 2
#
# August 7, 2019
#
# Clean up glossary.py by replacing series of print statements with a loop that runs through the dictionary
# keys and values. Add 5 more words to the glossary


glossary = {
    'foo': 'bar',
    'air': 'borne',
    'blue': 'falcon',
    'fizz': 'buzz',
    'war': 'eagle',
    'key': 'value',
    'star': 'bucks',
    'else': 'if',
    'list': 'tuple'
    }

for item in sorted(glossary.keys()):
    print(item + ": " + glossary[item])
