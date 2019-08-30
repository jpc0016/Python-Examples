# CH18 Example
#
# vigenere.py
# Demonstrate the Vigenere cipher on an input string and display its output
#import pyperclip

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

# Read input string and vigenere key
plaintext = input("Enter the plaintext string to encrypt: ")
# 'hello'
vigenere = input("Enter the vigenere key: ")
# 'pizza'

# Loop over each character of the plaintext and get the
# Vigenere subkeys of both the plaintext and key
plain_keys = []
for char in plaintext:
    # use uppercase char
    plain_key = character_key[char.upper()]
    plain_keys.append(plain_key)

vigenere_keys = []
for item in vigenere:
    vigenere_key = character_key[item.upper()]
    vigenere_keys.append(vigenere_key)

print(plain_keys)
# [7, 4, 11, 11, 14]
print(vigenere_keys)
# [15, 8, 25, 25, 0]

# Add the elements of each array together
encrypted_numbers = []
for i in range(0, len(plain_keys)):
    new = (plain_keys[i] + vigenere_keys[i]) % 26
    encrypted_numbers.append(new)

print(encrypted_numbers)
# [22, 12, 10, 10, 14]

encrypted = ""
for number in encrypted_numbers:
    # for 22
    for key, value in character_key.items():
        # for 'A':0 , 'B':1, ...
        # print(key) # A
        # print(value) # 0
        if value == number:
            # if 0 = 22
            encrypted += key

print(encrypted)
