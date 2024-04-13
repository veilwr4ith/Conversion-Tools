"""
################################################################################
#                                                                              #
# This code was created by veilwr4ith                                          #
#                                                                              #
# Vigenere Decoder                                                             #
#                                                                              #
################################################################################
"""

def vigenere_decode(ciphertext, keyword):
    keyword = keyword.upper()
    plaintext = ""
    keyword_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('A')
            
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            
            plaintext += decrypted_char
            keyword_index += 1
        else:
            plaintext += char
    return plaintext

ciphertext = input("Enter the ciphertext: ")
keyword = input("Enter the keyword: ")
decoded_text = vigenere_decode(ciphertext, keyword)
print("-" * 30)
print(f"Decoded String: {decoded_text}")

