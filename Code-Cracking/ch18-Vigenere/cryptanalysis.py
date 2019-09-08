# CH20 Example
#
# cryptanalysis.py
#
# v1.0 Draft
#
# Crack a ciphertext encrypted with the Vigenere cipher.  Program must detect
# patterns within the ciphertext

from collections import OrderedDict
from itertools import islice, cycle

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
    except ValueError:
        print("Period must be an integer!")
        continue
    else:
        break

# Analyze cipherText given the period of a key. Period is the key length
# Split cipherText into strings of key index.  There will be n number of groups
# where n is the period.  For a key length 4, there should be 3 groups of
# 1 mod(4), 2 mod(4), 3 mod(4), and 3 mod(4).
# groups is the list that holds each group of strings.
groups = []

# String splicing loop
# Value for each character in range 4, step over the string at an offset 'period'
for i in range(0, period):
    groups.append(cipherText[i: len(cipherText): period])

# Troubleshooting print statements [GOOD]
for j in range(0, period):
    print(groups[j])
print(" ")

# Custom dictionary shift function to move left each value to the adjacent key
def shift_dict(dict, shift):
    shift %= len(dict)
    return OrderedDict(
        (k, v)
        for k, v in zip(dict.keys(), islice(cycle(dict.values()), shift, None))
    )


# Create frequency analysis function.  Send each group through function as
# input.
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

# Implement all steps for each key character.  Loop from 0 to period
for num in range(0, period):

    counts = frequency_analysis(groups[num], len(groups[num]))

    print("\nLargest sum: " + str(max(counts)))
    print(" ")

    # Function frequency_analysis() works!!!  Now need to find largest value in list and return it's position.
    # This position will be used in character_key[key] to return plaintext character.
    # Check if correct index returned: 18
    print("Index of largest sum: " + str(counts.index(max(counts))))

    # should be 'S'
    print(character_key[counts.index(max(counts))])
    recovered_key.append(character_key[counts.index(max(counts))])


key = ''.join(recovered_key)
print(key)


# may need to call decrypt() function in vigenere-master and pass cipherText and
# most likely keys.  This would be done to brute force each possible key. Will need
# to import it: from vigenere import decrypt
# decrypt(cipherText, key)
