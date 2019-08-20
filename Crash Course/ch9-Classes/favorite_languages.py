# CH9 Exercise
#
# favorite_languages.py
#
# Python standard library
# Using OrderedDict() class from collections module.  This class keeps track of
# when key-value pairs are added
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

# for loop prints key-values in order
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
