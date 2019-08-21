# CH10 Example
#
# write_message.py
#
# Writing text to an empty file.
filename = 'programming.txt'

# Can open a file in read mode ('r'), write mode ('w'), append mode ('a'), or
# both read and write mode ('r+')
with open(filename, 'w') as f:
    f.write("I love programming.\n")
    f.write("I love creating new games.\n")
    f.close()

# Can add content to an existing file using append mode. Running this a second time
# will not add more text
with open(filename, 'a') as f:
    f.write("I also love finding meaning in large datasets.\n")
    f.write("I love creating apps that can run in a browser.\n")
    f.close()

# To add more text than the above, change 'w' in the first block to 'a' after
# previously running the code.  This will produce the following:
    # I love programming.
    # I love creating new games.
    # I also love finding meaning in large datasets.
    # I love creating apps that can run in a browser.
    # I love programming.
    # I love creating new games.
    # I also love finding meaning in large datasets.
    # I love creating apps that can run in a browser.
