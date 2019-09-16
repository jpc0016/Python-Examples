# John Cox
# CS 585 - Project 1
# vigenere-working.py
#
# v1.1
#
# Both encrypt() and decrypt() functions work on strings of variable size.
# Troubleshooting output remains in the code.  Is there a requirement to
# remove more characters than just spaces such as commas and quotes?
#
# Demonstrate the Vigenere cipher on an input string and display its output.
# Program must encrypt and decrypt strings of variable length

# Initialize character key dictionary to be used in encryption and decryption
#character_key = {'A': 0, 'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7,'I': 8,'J': 9,'K': 10,'L': 11,'M': 12,'N': 13,'O': 14,'P': 15,'Q': 16,'R': 17,'S': 18,'T': 19,'U': 20,'V': 21,'W': 22,'X': 23,'Y': 24,'Z': 25,}
character_key = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

# Read input string and vigenere keyplaintext and remove numbers, spaces, and
# special characters
in_plaintext = input("Enter the plaintext string to encrypt: ")
char_plaintext = ''.join(e for e in in_plaintext if e.isalnum())
plaintext = ''.join(f for f in char_plaintext if not f.isdigit())
# 'hello'
in_vigenere = input("Enter the vigenere key: ")
char_vigenere = ''.join(m for m in in_vigenere if m.isalnum())
vigenere = ''.join(n for n in char_vigenere if not n.isdigit())
# 'dog'

print("\n####################################")
print("\nEntered Plaintext: " + plaintext)
print("\n####################################")

#### VALIDATED TO WORK OVER VARIABLE KEY LENGTHS ####
def encrypt(plaintext, vigenere):
    """
    Encrypts plaintext using a vigenere key. Each character of the alphabet
    has a number code and the ciphertext is the sum of those codes.
    """

    # Enumerate characters of plaintext and store in plain_keys
    plain_keys = []
    # H, E, L, L, O
    for char in plaintext:
        # use uppercase char
        for value, letter in character_key.items():
            # if 'H' == 'A'
            if char.upper() == letter:
                plain_key = value
                # print(plain_key)
                plain_keys.append(plain_key)

        # plain_key = character_key.value(char.upper())
        # plain_keys.append(plain_key)

    # Enumerate characters of the key and store in vigenere_keys.  Enumerated
    # keys length should match plain_keys length
    vigenere_keys = []
    # D, O, G
    for item in vigenere:
        for value, letter in character_key.items():
            # if 'D' == 'A'
            if item.upper() == letter:
                vigenere_key = value
                print(vigenere_key)
                vigenere_keys.append(vigenere_key)

    # Troubleshooting:
    # Show enumerated plaintext and key
    print("\nEnumerated Plaintext")
    print(plain_keys)
    # [7, 4, 11, 11, 14]
    print("\nEnumerated Key")
    print(vigenere_keys)
    # [3, 14, 6]

    len_plain = len(plain_keys)
    # 5
    len_vig = len(vigenere_keys)
    # 3
    mod = len_plain % len_vig
    # 2

    # (len_plain - mod) / len_vig = number of iterations to fill vigenere_keys

    # Extend vigenere_keys to match plain_keys in length.  Check if
    # vigenere_keys is shorter than plain_keys
    if len_vig < len_plain:
        # (5 - 2) / 3 = 3/3 = 1
        iterations =  (len_plain - mod) / len_vig
        for iter in range(0, int(iterations)):
            for j in range(0, len_vig):
                if len(vigenere_keys) == len(plain_keys):
                    break
                else:
                    vigenere_keys.append(vigenere_keys[j])

    # If plain_keys < vigenere_keys, stop encryption at end of plain_keys
    # Entire program works if above condition is met
    print("\nPadded Vigenere Key: ")
    print(vigenere_keys)


    # Add the elements of each array together and mod 26.  If len(vigenere) is
    # less than len(plaintext), restart at begining of key.  If len(vigenere)
    # is greater than len(plaintext), stop at end of plaintext
    # Result is encrypted_numbers list

    encrypted_numbers = []
    for i in range(0, len(plain_keys)):
        new = (plain_keys[i] + vigenere_keys[i]) % 26
        encrypted_numbers.append(new)

    print("\nEnumerated Plaintext + Key")
    print(encrypted_numbers)
    # [10, 18, 17, 14, 2]

    # Convert enumerated plaintext + key into ciphertext string. Initialize
    # empty string
    encrypted = ""
    for number in encrypted_numbers:
        # for 10
        for key, value in character_key.items():
            # for 0: 'A' , 1: 'B', ...
            # print(key) # A
            # print(value) # 0
            if key == number:
                # if 0 = 10
                encrypted += value
    return encrypted


#### VALIDATED TO WORK OVER VARIABLE KEY LENGTHS ####
def decrypt(ciphertext, vigenere):
    """
    Decrypt the ciphertext by executing the encryption function backwards
    """

    # Enumerate characters of ciphertext and store in cipher_keys
    cipher_keys = []
    for char in ciphertext:
        # use uppercase char
        # KSROC
        for value, letter in character_key.items():
            # if 'K' == 'A'
            if char.upper() == letter:
                cipher_key = value
                cipher_keys.append(cipher_key)


        # cipher_key = character_key[char.upper()]
        # cipher_keys.append(cipher_key)


    # Enumerate characters of the vigenere key
    vigenere_keys = []
    for item in vigenere:

        for value, letter in character_key.items():
            # if 'D' == 'A'
            if item.upper() == letter:
                vigenere_key = value
                print(vigenere_key)
                vigenere_keys.append(vigenere_key)



        # vigenere_key = character_key[item.upper()]
        # vigenere_keys.append(vigenere_key)

    len_cipher = len(cipher_keys)
    # 5 (same as len(plain_keys))
    len_vig = len(vigenere_keys)
    # 3
    mod = len_cipher % len_vig
    # 2

    # (len_cipher - mod) / len_vig = number of iterations to fill vigenere_keys

    # Extend vigenere_keys to match cipher_keys in length.  Check if
    # vigenere_keys is shorter than cipher_keys
    if len_vig < len_cipher:
        # (5 - 2) / 3 = 3/3 = 1
        iterations =  (len_cipher - mod) / len_vig
        for iter in range(0, int(iterations)):
            for j in range(0, len_vig):
                if len(vigenere_keys) == len(cipher_keys):
                    break
                else:
                    vigenere_keys.append(vigenere_keys[j])

    # If cipher_keys < vigenere_keys, stop encryption at end of plain_keys
    # Entire program works if above condition is met
    print("\nPadded Vigenere Key: ")
    print(vigenere_keys)

    # # Troubleshooting:
    # # Show cipher keys [GOOD]
    # print("\nCipher Keys:")
    # print(cipher_keys)
    #
    # # Show vigenere keys [GOOD]
    # print("\nVigenere Keys:")
    # print(vigenere_keys)

    # Subtract the elements of each array and mod 26
    # Result is decrypted_numbers list
    decrypted_numbers = []
    for i in range(0, len(cipher_keys)):
        # Need to handle instance where cipher - key < 0
        # Example: B:1 - F:5 = -4
        if (cipher_keys[i] - vigenere_keys[i] < 0):
            new = 26 - (vigenere_keys[i] - cipher_keys[i])
        else:
            # W:22 - P:15 = H:7
            new = (cipher_keys[i] - vigenere_keys[i]) % 26
        decrypted_numbers.append(new)

    # Convert enumerated ciphertext - key into plaintext string. Initialize
    # empty string
    decrypted = ""
    for number in decrypted_numbers:
        # for 22
        for key, value in character_key.items():
            # for 0: 'A' , 1: 'B', ...
            # print(key) # A
            # print(value) # 0
            if key == number:
                # if 0 = 22
                decrypted += value
    return decrypted




# Test encrypt() function
crypto = encrypt(plaintext, vigenere)
print("\n####################################")
print("\nEncrypted text: " + crypto)
print("\n####################################")

# Test decrypt() function
plain = decrypt(crypto, vigenere)
print("\n####################################")
print("\nRecovered plaintext: " + plain)
print("\n####################################")
