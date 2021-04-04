#!/usr/bin/python3
# John
# rot-back.py
#
# Test case
# ciphertext: DDOUZBJWUPVFFPJOGJGLCPUSPZUIHDBUBHDJO
# rotation key: 131
#
#
# Rotate backward direction based on superimposed number key
import time

# Initialize character key dictionary to be used in encryption and decryption
character_key = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

# Prompt for cipherText and ensure it only contains characters.
in_cipherText = input("\nEnter the ciphertext: ")
char_cipherText = ''.join(e for e in in_cipherText if e.isalnum())
cipherText = ''.join(f for f in char_cipherText if not f.isdigit())

try:
    rotKey = int(input("Enter the rotation key (must be a number): "))
except ValueError:
    print("Rotation key must be a number!")

char_decrypt = ''.join(m for m in str(rotKey) if m.isalnum())
decrypt = ''.join(n for n in str(rotKey) if not n.isdigit())


print("\n####################################")
print("\nEntered Ciphertext: " + in_cipherText)
print("\nEntered Rotation key: " + str(rotKey))
print("\n####################################")
time.sleep(1)


# #### VALIDATED TO WORK OVER VARIABLE KEY LENGTHS ####
# def encrypt(plaintext, vigenere):
#     """
#     Encrypts plaintext using a vigenere key. Each character of the alphabet
#     has a number code and the ciphertext is the sum of those codes. Function
#     returns an encrypted ciphertext
#     """
#
#     # Enumerate characters of plaintext and store in plain_keys
#     plain_keys = []
#
#     for char in plaintext:
#         # use uppercase char
#         for value, letter in character_key.items():
#             if char.upper() == letter:
#                 plain_key = value
#                 plain_keys.append(plain_key)
#
#     # Enumerate characters of the key and store in vigenere_keys.  Enumerated
#     # keys length should match plain_keys length
#     vigenere_keys = []
#
#     for item in vigenere:
#         for value, letter in character_key.items():
#             if item.upper() == letter:
#                 vigenere_key = value
#                 vigenere_keys.append(vigenere_key)
#
#     # These are required calculations prior to extending vigenere_keys
#     len_plain = len(plain_keys)
#     len_vig = len(vigenere_keys)
#     mod = len_plain % len_vig
#
#     # Extend vigenere_keys to match plain_keys in length.  Check if
#     # vigenere_keys is shorter than plain_keys
#     if len_vig < len_plain:
#         iterations =  (len_plain - mod) / len_vig
#
#         for iter in range(0, int(iterations)):
#             for j in range(0, len_vig):
#                 # Exit loop when end is reached
#                 if len(vigenere_keys) == len(plain_keys):
#                     break
#                 else:
#                     vigenere_keys.append(vigenere_keys[j])
#
#     # Add the elements of each array together and mod 26.  If len(vigenere) is
#     # less than len(plaintext), restart at begining of key.  If len(vigenere)
#     # is greater than len(plaintext), stop at end of plaintext
#     # Result is encrypted_numbers list
#     encrypted_numbers = []
#     for i in range(0, len(plain_keys)):
#         new = (plain_keys[i] + vigenere_keys[i]) % 26
#         encrypted_numbers.append(new)
#
#     # Convert enumerated plaintext + key into ciphertext string by referencing
#     # the character_key dictionary
#     # Initialize empty string
#     encrypted = ""
#     for number in encrypted_numbers:
#         for key, value in character_key.items():
#             if key == number:
#                 encrypted += value
#
#     # Result of encrypt()
#     return encrypted
#
#
# #### VALIDATED TO WORK OVER VARIABLE KEY LENGTHS ####
def decrypt(ciphertext, key):
    """
    Decrypt the ciphertext by executing the rotation function backwards.
    Function returns a decrypted plaintext.
    """

    # Enumerate characters of ciphertext and store in cipher_keys
    cipher_keys = []
    for char in ciphertext:
        for value, letter in character_key.items():
            if char.upper() == letter:
                cipher_key = value
                cipher_keys.append(cipher_key)

    # Enumerate characters of the rotation key
    rot_keys = []
    for item in str(key):
        rot_keys.append(item)

        # for value, letter in character_key.items():
        #     if item.upper() == letter:
        #         vigenere_key = value
        #         vigenere_keys.append(vigenere_key)

    # Required calculations for extending rotation key
    len_cipher = len(cipher_keys)
    len_key = len(str(key))
    mod = len_cipher % len_key

    # Extend vigenere_keys to match cipher_keys in length.  Check if
    # vigenere_keys is shorter than cipher_keys
    if len_key < len_cipher:
        iterations =  (len_cipher - mod) / len_key
        for iter in range(0, int(iterations)):
            for j in range(0, len_key):
                # Exit loop when the end is reached
                if len(rot_keys) == len(cipher_keys):
                    break
                else:
                    rot_keys.append(rot_keys[j])

    # Subtract the elements of each array and mod 26
    # Result is decrypted_numbers list
    decrypted_numbers = []
    for i in range(0, len(cipher_keys)):
        # Handle instance where cipher - key < 0
        if (cipher_keys[i] - int(rot_keys[i]) < 0):
            new = 26 - (int(rot_keys[i]) - cipher_keys[i])
        else:
            new = (cipher_keys[i] - int(rot_keys[i])) % 26
        decrypted_numbers.append(new)

    # Convert enumerated ciphertext - key into plaintext string. Initialize
    # empty string
    decrypted = ""
    for number in decrypted_numbers:
        for key, value in character_key.items():
            if key == number:
                decrypted += value

    # Result of decrypt()
    return decrypted


# # Encrypt plaintext
# crypto = encrypt(plaintext, vigenere)
# print("\n####################################")
# print("\nEncrypted text: " + crypto)
# print("\n####################################")

# # Decrypt ciphertext
plain = decrypt(in_cipherText, rotKey)
print("\n####################################")
print("\nRecovered plaintext: " + plain)
print("\n####################################")
