# John Cox
# CS 585 - Project 1
# cryptanalysis-troubleshoot.py
#
# v2.1 Draft
#
# Crack a ciphertext encrypted with the Vigenere cipher.  Program must detect
# patterns within the ciphertext.
#
# This script is identical to cryptanalysis.py only with more comments and troubleshooting
# print statements
#
# NOTE:
# decrypt.py must be in same directory as cryptanalysis-troubleshoot.py

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

# Prompt for cipherText and ensure it only contains characters.
in_cipherText = input("\nEnter the ciphertext: ")
char_cipherText = ''.join(e for e in in_cipherText if e.isalnum())
cipherText = ''.join(f for f in char_cipherText if not f.isdigit())

print("Sanitized ciphertext: " + cipherText)

# Prompt for period and check for correct type.  If incorrect type, continue
# to beginning of while loop.  If correct type, break loop.
while True:
    try:
        input_period = input("\nEnter period of the Vigenere key: ")
        print("\nInput period: " + str(input_period))
        period = int(input_period)
        print("\nInput period: " + str(input_period))
    except ValueError:
        print("Period must be an integer!")
        continue
    else:
        break

# Start wall clock and CPU clock
clock_start = datetime.datetime.now()
cpu_start = time.process_time_ns()

# Analyze cipherText given the period of a key. Period is the key length
# Split cipherText into strings of key index.  There will be n number of groups
# where n is the period.  For a key length 4, there should be 3 groups of
# 1 mod(4), 2 mod(4), 3 mod(4), and 3 mod(4).
# groups is the list that holds each group of strings.
groups = []

##### GOOD #####
# value for each character in range 4, step over the string at an offset 'period'
for i in range(0, period):
    groups.append(cipherText[i: len(cipherText): period])

# Troubleshooting print statements [GOOD]
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
# TESTING DICTIONARY SHIFT#
# first_dict = {'a': 5, 'b': 10, 'c': 15}
# print(first_dict)
# second_dict = shift_dict(first_dict, 1)
# print(second_dict)

##### WORKING [ALMOST DONE]#####
# Now have 3 groups of indexed characters.
# Create frequency analysis function.  Send each group through function as
# input. May need to create a seperate file and import it since it could
# get very large
def frequency_analysis(text, totalCharacters):
    """
    Count number of times a letter appears in the cipherText. This function returns
    the most likely shift value for the key at a given index. The shift value
    corresponds to a letter in character_key
    """
    # Initialize frequency count
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    # Dictionary of English letters by frequency. 'E' is most common. 'Z' is most
    # uncommon.  Try letter strings instead of numbers
    englishFrequency = {'A': 0.080, 'B': 0.015, 'C': 0.030, 'D': 0.040, 'E': 0.130, 'F': 0.020, 'G': 0.015, 'H': 0.060, 'I': 0.065, 'J': 0.005, 'K': 0.005, 'L': 0.035, 'M': 0.030, 'N': 0.070, 'O': 0.080, 'P': 0.020, 'Q': 0.002, 'R': 0.065, 'S': 0.060, 'T': 0.090, 'U': 0.030, 'V': 0.010, 'W': 0.015, 'X': 0.005, 'Y': 0.020, 'Z': 0.002}
    # Old table
    # englishFrequency = {0: 0.080, 1: 0.015, 2: 0.030, 3: 0.040, 4: 0.130, 5: 0.020, 6: 0.015, 7: 0.060, 8: 0.065, 9: 0.005, 10: 0.005, 11: 0.035, 12: 0.030, 13: 0.070, 14: 0.080, 15: 0.020, 16: 0.002, 17: 0.065, 18: 0.060, 19: 0.090, 20: 0.030, 21: 0.010, 22: 0.015, 23: 0.005, 24: 0.020, 25: 0.002}

    # Count letters in cipherText group [GOOD]
    for char in text:
        letterCount[char.upper()] += 1

    # Troubleshooting prints
    print("Current letterCount: ")
    print(letterCount)

    # Find letter frequency from letterCount.  Divide each letter by [GOOD]
    # total number of letters.  Round to 4 decimal places
    letterFrequency = OrderedDict()
    for key, value in letterCount.items():
        letterFrequency[key] = round((value/totalCharacters), 4)

    # Troubleshooting prints
    print("\nletterFrequency: ")
    print(letterFrequency)
    print(" ")

    # letterFrequency:
    # OrderedDict([('A', 0.0), ('B', 0.0789), ('C', 0.0), ('D', 0.0526), ('E', 0.0526), ('F', 0.0263), ('G', 0.0263), ('H', 0.1053), ('I', 0.0), ('J', 0.0263), ('K', 0.1053), ('L', 0.0789), ('M', 0.0),
    # ('N', 0.0263), ('O', 0.0789), ('P', 0.0789), ('Q', 0.0263), ('R', 0.0789), ('S', 0.0), ('T', 0.0), ('U', 0.0789), ('V', 0.0263), ('W', 0.0263), ('X', 0.0263), ('Y', 0.0), ('Z', 0.0)])

    all_sums = []
    # Now need to multiply each letter of letterFrequency by englishFrequency and sum
    # them all up.  Repeat this 26 times after shifting each entry of letterFrequency.
    # Run initial test of sum without any shifting  [INITIAL TEST IS GOOD]
    ####################
    # WORKING ON SHIFTING DICTIONARY LEFT IN A LOOP 26 TIMES.  THIS WILL BE
    # HANDLED IN AN OUTER LOOP FOR RANGE(0, 25).  SUM OF EACH DICTIONARY
    # ROTATION IS STORED IN all_sums
    ####################
    for number in range(0,26):

        sum = 0
        for key, value in letterFrequency.items():
            # print("\nenglishFrequency[" + str(key) + "]: " + str(englishFrequency[key]))
            # print("value: " + str(value))
            # print("Pre-Sum: " + str(sum))
            sum += englishFrequency[key] * value # 0.080 * 0
            # print("Post-Sum: " + str(sum))

        # Add to list of sums
        all_sums.append(sum)

        # Shift letterFrequency dictionary by 1
        letterFrequency = shift_dict(letterFrequency, 1)

    return all_sums


recovered_key = []
list_of_top3 = []

# Implement all steps for each key character.  Loop from 0 to period
for num in range(0, period):

    counts = frequency_analysis(groups[num], len(groups[num]))

    # Need to get top 3 values from counts [GOOD]
    print("All Sums (counts): ")
    print(counts)

    # Sorted sums sorts from highest to lowest [GOOD]
    sorted_sums = sorted(counts, reverse=True)
    print("\nSorted Sums: ")
    print(sorted_sums)

    # Need to convert top 3 from numbers to letters
    first_3 = sorted_sums[:3]
    top_3 = []

    for item in first_3:
        top_3.append(character_key[counts.index(item)])




    print("\nTop 3: ")
    print(top_3)
    list_of_top3.append(top_3)

    # Retrieving max value works
    print("\nLargest sum: " + str(max(counts)))
    print(" ")

    # Function frequency_analysis() works!!!  Now need to find largest value in list and return it's position.
    # This position will be used in character_key[key] to return plaintext character.
    # Check if correct index returned: 18
    print("Index of largest sum: " + str(counts.index(max(counts))))

    # should be 'S'
    print(character_key[counts.index(max(counts))])
    print("----------------------------------------------------------------------------------------------------------------------\n")

    # May not need to append the highest character yet.  Should use itertools to
    # try all possible combinations.  recovered_key might be appended to another list
    # called possible_keys[]
    # recovered_key.append(character_key[counts.index(max(counts))])


# key = ''.join(recovered_key)
# print(key)

# Check the list of top 3 sums for each letter in the key
print("\nList of Top 3 Sums for each letter (list_of_top3): ")
print(list_of_top3)

# Use itertools.product() [GOOD]
print("\nList of all possible key combinations (joined_keys): ")
all_keys = list(itertools.product(*list_of_top3))

joined_keys = []
for key_list in all_keys:
    key_attempt = ''.join(key_list)
    joined_keys.append(key_attempt)


print(joined_keys)
print(" ")


# Brute force the ciphertext with each possible key in joined_keys
# Open dictionary.txt for word search in each decrypted string
# Initialize table of dictionary word counts.  The index with the highest count
# will return its corresponding recovered plaintext indexed in plaintext_array
filename = 'doc/dictionary.txt'
table_of_counts = []
plaintext_array = []
for attempt in joined_keys:

    with open(filename) as f:
        english_word_count = 0
        words = f.read().splitlines()
        # Call decrypt function from vigenere
        plain = decrypt(cipherText, attempt)
        plaintext_array.append(plain)
        #print(words)

        #print("English word count: " + str(english_word_count))

        # if the dictionary word is in the string, increment english_word_count
        # break out of loop and file
        #print(plain.count('DANCE'))

        # Iterate over each word in dictionary.txt
        for word in words:
            if plain.count(word) > 0:
                english_word_count += 1

        # Add total english word count to table when done searching all words
        table_of_counts.append(english_word_count)
        f.close()

print("\nEnglish word counts (table_of_counts): ")
print(table_of_counts)
print("\nHighest english word count: " + str(max(table_of_counts)))

# Need to index the max count to retrieve proper plaintext
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
    #         if english_word_count > 3:
    #             print("\n####################################")
    #             print("\nRecovered Plaintext: " + plain)
    #             print("\n####################################")
    #             break
    #         else:
    #             # check plaintext for occurance of word
    #             if plain.count(word) > 0:
    #                 #print(word)
    #                 english_word_count += 1
    #             continue
    #
    #         # Break for loop when all words are attempted
    #         break
    #     f.close()
    #
    # if english_word_count > 3:
    #     break
    # else:
    #     continue
