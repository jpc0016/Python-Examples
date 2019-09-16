# Vigenère Cipher

|     |     |
|-----|-----|
|**vigenere.py**|[![Version](https://img.shields.io/badge/version-1.5-blue)]()|
|**cryptanalysis.py**|[![Version](https://img.shields.io/badge/version-2.0-orange)]()|

Create two programs. One program encrypts and decrypts messages using the Vigenère cipher.  The other program is to break the Vigenère cipher given a ciphertext and key period (length).

Script 1 Task: Demonstrate the Vigenere cipher on an input string and display its output. Program must encrypt and decrypt strings of variable length.

Script 2 Task: Crack a ciphertext encrypted with the Vigenere cipher.  Program must detect patterns within the ciphertext.

## Introduction
The Vigenère cipher is like the Caeser cipher but uses a key phrase instead of a number.

From `2.0 Cryptography.pdf`:
* Message: THE BOY HAS THE BALL
* Key:      VIG

* using Cæsar cipher shift for each letter:

      Plain THEBOYHASTHEBALL

      Key: VIGVIGVIGVIGVIGV

      cipher OPKWWECIYOPKWIRG



## Initial Requirements
Taken from assignment page:

CS 485/585 Project 1 (100 points)

Implement the Vigènere cipher (Encryption and decryption).
Write another program, which breaks the Vigènere cipher. Suppose that you know the period is 3.

You are to deliver:

1.  A (commented) code listing (hard copy).

2.  Source and binary via Canvas.

3.  The screen shots of your test cases (hard copy). Make sure that you test edge cases.

Your code should be thoroughly commented.

Your score on this assignment will include consideration of the correctness of your code, readability of the code, and quality of internal documentation (commenting).


## Additional Requirements from Professor
* Remove all spaces in plaintext before encrypting it.

* Binary file is not required if Python is used.

* *Period* is a required parameter in the second program

## Revision History

|  Script | Version | Description of Changes |
|  ------ | ------ | ------ |
|  vigenere.py | 0.5 | Draft |  
|   | 1.0 | Working encrypt() and decrypt() functions on variable length input. |
|   | 1.1 | Add input validation for plaintext and key. Ensure numbers, spaces, and special characters are stripped. |
|   | 1.5 | Swapped key, values in character_key |  
|  cryptanalysis.py | 0.5 | Draft |   
|   | 1.0 | Working frequency_analysis() function on ciphertext and key length |  
|   | 2.0 | Add plaintext recovery and comprehensive key checking |


## To Do

* Continue comment cleanup
