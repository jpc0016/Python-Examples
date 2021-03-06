# CH6 Example
#
# languages.py
#
# Track favorite programming languages for users and print a
# favorite one.
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c++'],
    'edward': ['ruby', 'go'],
    'phil': ['python'],
    'jacob': [],
    }

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")



# .items() returns a list of key-value pairs
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(name.title() + "'s favorite language is " + languages[0].title() + ".\n")
    elif len(languages) == 0:
        print(name.title() + " hates coding.\n")
    else:
        # Note: all value items in favorite_languages must be lists.  If not, single items like
        # 'C++' will output each character one line at a time.
        print(name.title() + "'s favorite languages are: ")
        for language in languages:
            print("\t" + language.title())

# .keys() returns only the dictionary keys
# 'for name in favorite_languages:' produces the same output as below so .keys() is redundant
# in this case.
# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages:
#     print(name.title())
#
#     if name in friends:
#         print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")


# Can sort dictionary keys by using sorted([dictionary name])
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")

# Can sort through dictionary values using .values() method
# 'Python' is listed twice.  Repeats are not checked.  Use set([dictionary name]) to check for repeat values
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())
