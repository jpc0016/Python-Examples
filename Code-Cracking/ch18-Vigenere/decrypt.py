character_key = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

def decrypt(ciphertext, vigenere):
    """
    Decrypt the ciphertext by executing the encryption function backwards
    """

    # Enumerate characters of ciphertext and store in cipher_keys
    cipher_keys = []
    for char in ciphertext:
        # use uppercase char
        for value, letter in character_key.items():
            if char.upper() == letter:
                cipher_key = value
                cipher_keys.append(cipher_key)

    # Enumerate characters of the vigenere key
    vigenere_keys = []
    for item in vigenere:

        for value, letter in character_key.items():
            if item.upper() == letter:
                vigenere_key = value
                vigenere_keys.append(vigenere_key)

    len_cipher = len(cipher_keys)
    len_vig = len(vigenere_keys)
    mod = len_cipher % len_vig


    # (len_cipher - mod) / len_vig = number of iterations to fill vigenere_keys

    # Extend vigenere_keys to match cipher_keys in length.  Check if
    # vigenere_keys is shorter than cipher_keys
    if len_vig < len_cipher:
        iterations =  (len_cipher - mod) / len_vig
        for iter in range(0, int(iterations)):
            for j in range(0, len_vig):
                if len(vigenere_keys) == len(cipher_keys):
                    break
                else:
                    vigenere_keys.append(vigenere_keys[j])

    # If cipher_keys < vigenere_keys, stop encryption at end of plain_keys

    # Subtract the elements of each array and mod 26
    # Result is decrypted_numbers list
    decrypted_numbers = []
    for i in range(0, len(cipher_keys)):
        # Need to handle instance where cipher - key < 0
        if (cipher_keys[i] - vigenere_keys[i] < 0):
            new = 26 - (vigenere_keys[i] - cipher_keys[i])
        else:
            new = (cipher_keys[i] - vigenere_keys[i]) % 26
        decrypted_numbers.append(new)

    # Convert enumerated ciphertext - key into plaintext string. Initialize
    # empty string
    decrypted = ""
    for number in decrypted_numbers:
        for key, value in character_key.items():
            if key == number:
                decrypted += value
    return decrypted
