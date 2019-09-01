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

# Retreive the ciphertext

ciphertext = input("Enter the ciphertext: ")
period = input("Enter period of the Vigenere key: ")
