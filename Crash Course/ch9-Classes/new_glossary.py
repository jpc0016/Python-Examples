# CH9 Exercise 9-13
#
# new_glossary.py
# August 20, 2019
#
# Rewrite glossary.py using an ordered dictionary

from collections import OrderedDict

# initialize the ordered dictionary first before adding key-value pairs
glossary = OrderedDict()

# remember brackets for explicitly entering key-values
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

for item in glossary.keys():
    print(item + ": " + glossary[item])
