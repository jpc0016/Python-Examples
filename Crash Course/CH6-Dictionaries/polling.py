# CH6 Exercise 6-6: Polling
#
# August 7, 2019
#
# Given languages.py
# Make list of people who should take favorite languages poll.  Include some names in the dictionary
# and some that are not

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

new_list = ['curt', 'john', 'jen', 'danesh', 'phil', 'jeff']

# loop through new_list and check if they took the poll.  If their name exists in favorite_languages,
# thank them for taking the poll.  If not, ask them to take the poll.
for name in new_list:
    if name in favorite_languages.keys():
        print("Thanks for taking the poll, " + name.title() + "!\n")
    else:
        print(name.title() + ", please take the poll.\n")
