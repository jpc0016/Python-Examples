# John Cox
# CS 585 - Project 1
# cryptanalysis.py
#
# v2.0 Draft
#
# Crack a ciphertext encrypted with the Vigenere cipher.  Program must detect
# patterns within the ciphertext.

import itertools
from decrypt import *
from collections import OrderedDict
from itertools import islice, cycle
import datetime
import time

# Initialize character key dictionary to be used in encryption and decryption
character_key = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

"""
Test with cipherText:
'SECGLEYWAMNRJUOTBXLEGGMRQFIHJZCIWLPNFWYETBFGLAYYWTXYGHENLMBRVXZRFLYGAFMGMGHRVBGRSGSBMMUYCTVBMMKHAVESWXNGZTNFSECGLEYQSGWRSGXTGWUAUXUAVZIGAFMHHAYEWZLNTUCAYFYGJRCAYMIQGLIZWWUAUXGBNXMGGBGVLTNRKXSZGNL'

Plaintext:
'a little jitterbug jerron seymour gives vanderbilt the lead look at the defense tim stunned i mean you talk about quick feet thats a little dance and go dance and go tims up here grabbing me trying to do some dance moves to imitate seymour'

Key: 'stun'
"""

# Prompt for cipherText
cipherText = input("Enter the ciphertext: ")

# Prompt for period and check for correct type.  If incorrect type, continue
# to beginning of while loop.  If correct type, break loop.
while True:
    try:
        input_period = input("Enter period of the Vigenere key: ")
        period = int(input_period)
        clock_start = datetime.datetime.now()
        cpu_start = time.process_time_ns()
    except ValueError:
        print("Period must be an integer!")
        break
    else:
        break

# Analyze cipherText given the period of a key. Period is the key length
# Split cipherText into strings of key index.  There will be n number of groups
# where n is the period.  For a key length 4, there should be 3 groups of
# 1 mod(4), 2 mod(4), 3 mod(4), and 3 mod(4).
# groups is the list that holds each group of strings.
groups = []

# String splicing loop
# value for each character in range 4, step over the string at an offset 'period'
for i in range(0, period):
    groups.append(cipherText[i: len(cipherText): period])

# Print each text group
print(" ")
for j in range(0, period):
    print(groups[j])
print(" ")

# Custom dictionary shift function
def shift_dict(dict, shift):
    shift %= len(dict)
    return OrderedDict(
        (k, v)
        for k, v in zip(dict.keys(), islice(cycle(dict.values()), shift, None))
    )

# Create frequency analysis function.  Send each group of text through
# function as input. Returns a list of 26 sums for each letter position in
# the alphabet. Each letter frequency in the group string is multiplied by the
# corresponding position of englishFrequency.
#
# Example:
# For unshifted dictionary, suppose it is OrderedDict([('A', 0.0), ('B', 0.0789), ('C', 0.0)])
# and englishFrequency is static: englishFrequency = {'A': 0.080, 'B': 0.015, 'C': 0.030}
#
# then sum = (0.0 * 0.080) + (0.0789 * 0.015) + (0.0 * 0.030)
#
# The ordered dictionary is shifted in the next step:
# OrderedDict([('B', 0.0789), ('C', 0.0), ('A', 0.0)])
def frequency_analysis(text, totalCharacters):
    """
    Count number of times a letter appears in the cipherText. This function returns
    the most likely shift value for the key at a given index. The shift value
    corresponds to a letter in character_key
    """
    # Initialize frequency count
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    # Static dictionary of English letters by frequency. 'E' is most common. 'Z' is most
    # uncommon.
    englishFrequency = {'A': 0.080, 'B': 0.015, 'C': 0.030, 'D': 0.040, 'E': 0.130, 'F': 0.020, 'G': 0.015, 'H': 0.060, 'I': 0.065, 'J': 0.005, 'K': 0.005, 'L': 0.035, 'M': 0.030, 'N': 0.070, 'O': 0.080, 'P': 0.020, 'Q': 0.002, 'R': 0.065, 'S': 0.060, 'T': 0.090, 'U': 0.030, 'V': 0.010, 'W': 0.015, 'X': 0.005, 'Y': 0.020, 'Z': 0.002}

    # Count letters in cipherText group
    for char in text:
        letterCount[char.upper()] += 1


    # Find letter frequency from letterCount.  Divide each letter by
    # total number of letters.  Round to 4 decimal places
    letterFrequency = OrderedDict()
    for key, value in letterCount.items():
        letterFrequency[key] = round((value/totalCharacters), 4)

    # letterFrequency:
    # OrderedDict([('A', 0.0), ('B', 0.0789), ('C', 0.0), ('D', 0.0526), ('E', 0.0526), ('F', 0.0263), ('G', 0.0263), ('H', 0.1053), ('I', 0.0), ('J', 0.0263), ('K', 0.1053), ('L', 0.0789), ('M', 0.0),
    # ('N', 0.0263), ('O', 0.0789), ('P', 0.0789), ('Q', 0.0263), ('R', 0.0789), ('S', 0.0), ('T', 0.0), ('U', 0.0789), ('V', 0.0263), ('W', 0.0263), ('X', 0.0263), ('Y', 0.0), ('Z', 0.0)])

    all_sums = []
    # Multiply each letter of letterFrequency by englishFrequency and sum
    # them all up.  Repeat this 26 times after shifting each entry of letterFrequency.
    # Highest sum is the most likely character of the key
    for number in range(0,26):

        sum = 0
        for key, value in letterFrequency.items():
            sum += englishFrequency[key] * value

        # Add to list of sums
        all_sums.append(sum)

        # Shift letterFrequency dictionary by 1
        letterFrequency = shift_dict(letterFrequency, 1)

    return all_sums


# Implement all steps for each key character.  Loop from 0 to period
list_of_top3 = []
for num in range(0, period):

    # Retrieve the list of all sums (all_sums)
    counts = frequency_analysis(groups[num], len(groups[num]))

    # Sort list of sums from highest to lowest
    sorted_sums = sorted(counts, reverse=True)

    # Convert top 3 sums from numbers to letters and add to top_3 characters list
    first_3 = sorted_sums[:3]
    top_3 = []

    for item in first_3:
        top_3.append(character_key[counts.index(item)])

    # Add top_3 characters list to total top 3 list.  This is a list of lists.
    list_of_top3.append(top_3)



# Check the list of top 3 sums for each letter position in the key
print(" ")
print("\nList of Top 3 Sums for each letter (list_of_top3): ")
print(list_of_top3)
print(" ")

# Use itertools.product()
all_keys = list(itertools.product(*list_of_top3))

joined_keys = []
for key_list in all_keys:
    key_attempt = ''.join(key_list)
    joined_keys.append(key_attempt)



# Brute force the ciphertext with each possible key in joined_keys
# Open dictionary.txt for word search in each decrypted string
# Initialize table of dictionary word counts (table_of_counts).  The index
# with the highest count will return its corresponding recovered plaintext
# indexed in plaintext_array
filename = 'doc/dictionary.txt'
table_of_counts = []
plaintext_array = []

for attempt in joined_keys:

    with open(filename) as f:
        english_word_count = 0
        words = f.read().splitlines()
        # Call decrypt function from vigenere and add it to plaintext_array
        plain = decrypt(cipherText, attempt)
        plaintext_array.append(plain)

        # Iterate over each word in dictionary.txt
        # If the dictionary word is in the string, increment english_word_count
        for word in words:
            if plain.count(word) > 0:
                english_word_count += 1

        # Add total english word count to table when done searching all words
        table_of_counts.append(english_word_count)
        f.close()


# Index the max count to retrieve proper plaintext
print(table_of_counts.index(max(table_of_counts)))
print("\n####################################")
print("\nRecovered Plaintext: " + plaintext_array[table_of_counts.index(max(table_of_counts))])
print("\nKey used: " + joined_keys[table_of_counts.index(max(table_of_counts))])
print("\n####################################")

# Calculate and display time differences
clock_end = datetime.datetime.now()
time_diff = clock_end - clock_start
cpu_end = time.process_time_ns()
cpu_delta = cpu_end - cpu_start

print("\nWall clock start time: ", clock_start)
print("Wall clock end time: ", clock_end)
print("Wall clock difference: ", time_diff)

print("\nCPU start time (ns): ", cpu_start)
print("CPU end time (ns): ", cpu_end)
print("Processing time: ", cpu_delta)
