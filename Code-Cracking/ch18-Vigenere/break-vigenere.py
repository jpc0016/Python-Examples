# CH18 Example
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

# Initialize character key to be used in encryption and decryption
character_key = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
            'H': 7,
            'I': 8,
            'J': 9,
            'K': 10,
            'L': 11,
            'M': 12,
            'N': 13,
            'O': 14,
            'P': 15,
            'Q': 16,
            'R': 17,
            'S': 18,
            'T': 19,
            'U': 20,
            'V': 21,
            'W': 22,
            'X': 23,
            'Y': 24,
            'Z': 25,
}

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

print("Entered ciphertext: " + ciphertext)
print("Period: " + str(period))
print(" ")

# Analyze ciphertext given the period of a key. Period is the key length
# Split ciphertext into strings of key index.  There will be n number of groups
# where n is the period.  For a key length 3, there should be 3 groups of
# 1 mod(3), 2 mod(3), and 3 mod(3)

# Create the groups
groups = [[] for i in range(1, period)]

for num in range(1, period):
    print("\nGroup " + str(period) + ":")
    print(groups[period])
# iterate characters over ciphertext [GOOD]
# for char in ciphertext:
#     print(char)

# for number in range(1, period):
# for index, number in enumerate(ciphertext):
#     if index % period == 0:
