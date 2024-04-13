"""
################################################################################
#                                                                              #
# This code was created by veilwr4ith                                          #
#                                                                              #
# XOR Decoder                                                                  #
#                                                                              #
################################################################################
"""

def xor_decode(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        plaintext += chr(ord(char) ^ key)
    return plaintext

ciphertext = input("Enter the ciphertext: ")
key = int(input("Enter the key (an integer): "))
decoded_text = xor_decode(ciphertext, key)
print("-" * 30)
print(f"Decoded String: {decoded_text}")
