# CH20 Example
#
# break-vigenere.py
#
# v0.1 Draft
#
# Crack a ciphertext encrypted with the Vigenere cipher.  Program must detect
# patterns within the ciphertext
#
# According to Dr. Zhu, period (size of vigenere key) is given?????  Need to
# confirm

# Follow steps here:
# https://artofproblemsolving.com/community/c1671h1005767_cracking_the_vigenere_cipher_knowing_the_keyword_length

# Initialize character key dictionary to be used in encryption and decryption
character_key = {'A': 0, 'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7,'I': 8,'J': 9,'K': 10,'L': 11,'M': 12,'N': 13,'O': 14,'P': 15,'Q': 16,'R': 17,'S': 18,'T': 19,'U': 20,'V': 21,'W': 22,'X': 23,'Y': 24,'Z': 25,}


"""
Test with ciphertext: 'KSELXAVHSHHERIGQRZKWYLGIUOFBPAWVKUSYPMTXAHHFYRQGOZSHAGBPKLHYKOXGHUOCUNFOJVZDHERIHDPEEIZKSXHGSBBAPPKUGUFOROAKPOEES'

Plaintext: 'Hey I just met you and this is crazy but heres my number so call me maybe Its hard to look right at you baby But heres my number so call me maybe'
Key: 'dog'
"""

# Prompt for ciphertext
ciphertext = input("Enter the ciphertext: ")

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

# Troubleshooting print statements
print("Entered ciphertext: " + ciphertext)
print("Period: " + str(period))
print(" ")

# Analyze ciphertext given the period of a key. Period is the key length
# Split ciphertext into strings of key index.  There will be n number of groups
# where n is the period.  For a key length 3, there should be 3 groups of
# 1 mod(3), 2 mod(3), and 3 mod(3).  groups is the list that holds each group
# of strings.
groups = []

##### GOOD #####
# for each character in range 3, step over the string at an offset 'period'
for i in range(0, period):
    groups.append(ciphertext[i: len(ciphertext): period])

# Troubleshooting print statements [GOOD]
for j in range(0, period):
    print(groups[j])
print(" ")

##### WORKING #####
# Now have 3 groups of indexed characters.
# Create frequency analysis function.  Send each group through function as
# input. May need to create a seperate file and import it since it could
# get very large
def frequency_analysis(text):
    """
    Count number of times a letter appears in the ciphertext.
    """
    # Initialize frequency count
    letterFrequency = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    # Order of English letters by frequency. 'E' is most common. 'Z' is most
    # uncommon
    englishFrequency = 'ETAOINSHRDLUCMWFGYPBVKJXQZ'

    # Count letters in ciphertext group [GOOD]
    for char in text:
        letterFrequency[char.upper()] += 1

    return letterFrequency


counts = frequency_analysis(groups[0])
print(counts)
