# CH18 Example
#
# vigenere-working.py
# Demonstrate the Vigenere cipher on an input string and display its output.
# Program must encrypt and decrypt strings of variable length
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

# Read input string and vigenere keyplaintext
plaintext = input("Enter the plaintext string to encrypt: ")
# 'hello'
vigenere = input("Enter the vigenere key: ")
# 'pizza'

##### CURRENTLY ONLY WORKS FOR STRINGS OF SAME SIZE #####
def encrypt(plaintext, vigenere):
    """
    Encrypts plaintext using a vigenere key. Each character of the alphabet
    has a number code and the ciphertext is the sum of those codes.
    """

    # Enumerate characters of plaintext and store in plain_keys
    plain_keys = []
    for char in plaintext:
        # use uppercase char
        plain_key = character_key[char.upper()]
        plain_keys.append(plain_key)

    # Enumerate characters of the key and store in vigenere_keys
    vigenere_keys = []
    for item in vigenere:
        vigenere_key = character_key[item.upper()]
        vigenere_keys.append(vigenere_key)

    # Troubleshooting:
    # Show enumerated plaintext and key
    print("\nEnumerated Plaintext")
    print(plain_keys)
    # [7, 4, 11, 11, 14]
    print("\nEnumerated Key")
    print(vigenere_keys)
    # [15, 8, 25, 25, 0]

    # Add the elements of each array together and mod 26
    # Result is encrypted_numbers list
    encrypted_numbers = []
    for i in range(0, len(plain_keys)):
        new = (plain_keys[i] + vigenere_keys[i]) % 26
        encrypted_numbers.append(new)

    print("\nEnumerated Plaintext + Key")
    print(encrypted_numbers)
    # [22, 12, 10, 10, 14]

    # Convert enumerated plaintext + key into ciphertext string. Initialize
    # empty string
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
    return encrypted


##### CURRENTLY ONLY WORKS FOR STRINGS OF SAME SIZE #####
def decrypt(ciphertext, vigenere):
    """
    Decrypt the ciphertext by executing the encryption function backwards
    """

    # Enumerate characters of ciphertext and store in cipher_keys
    cipher_keys = []
    for char in ciphertext:
        # use uppercase char
        cipher_key = character_key[char.upper()]
        cipher_keys.append(cipher_key)

    # Troubleshooting:
    # Show cipher keys [GOOD]
    print("Cipher Keys:")
    print(cipher_keys)




# Test encrypt() function
crypto = encrypt(plaintext, vigenere)
print("Encrypted text: " + crypto)

# Test decrypt() function
decrypt(crypto, vigenere)
