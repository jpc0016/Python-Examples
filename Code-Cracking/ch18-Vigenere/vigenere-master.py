# John Cox
# CS 585 - Project 1
# vigenere-master.py
#
# v1.0 rev Draft
#
# Demonstrate the Vigenere cipher on an input string and display its output.
# Program must encrypt and decrypt strings of variable length

# Initialize character key dictionary to be used in encryption and decryption
character_key = {'A': 0, 'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7,'I': 8,'J': 9,'K': 10,'L': 11,'M': 12,'N': 13,'O': 14,'P': 15,'Q': 16,'R': 17,'S': 18,'T': 19,'U': 20,'V': 21,'W': 22,'X': 23,'Y': 24,'Z': 25,}

# Read input string and vigenere keyplaintext and remove spaces
plaintext = input("Enter the plaintext string to encrypt: ")
plaintext = plaintext.replace(" ", "")

vigenere = input("Enter the vigenere key: ")
vigenere = vigenere.replace(" ", "")


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
    for char in plaintext:
        # use uppercase char
        plain_key = character_key[char.upper()]
        plain_keys.append(plain_key)

    # Enumerate characters of the key and store in vigenere_keys.  Enumerated
    # keys length should match plain_keys length
    vigenere_keys = []
    for item in vigenere:
        vigenere_key = character_key[item.upper()]
        vigenere_keys.append(vigenere_key)


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


    # Add the elements of each array together and mod 26.  If len(vigenere) is
    # less than len(plaintext), restart at begining of key.  If len(vigenere)
    # is greater than len(plaintext), stop at end of plaintext
    # Result is encrypted_numbers list
    encrypted_numbers = []
    for i in range(0, len(plain_keys)):
        new = (plain_keys[i] + vigenere_keys[i]) % 26
        encrypted_numbers.append(new)


    # Convert enumerated plaintext + key into ciphertext string. Initialize
    # empty string
    encrypted = ""
    for number in encrypted_numbers:
        # for 22
        for key, value in character_key.items():
            # for 'A':0 , 'B':1, ...
            if value == number:
                # if 0 = 22
                encrypted += key
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
        cipher_key = character_key[char.upper()]
        cipher_keys.append(cipher_key)


    # Enumerate characters of the vigenere key
    vigenere_keys = []
    for item in vigenere:
        vigenere_key = character_key[item.upper()]
        vigenere_keys.append(vigenere_key)

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
            # for 'A':0 , 'B':1, ...
            # print(key) # A
            # print(value) # 0
            if value == number:
                # if 0 = 22
                decrypted += key
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
