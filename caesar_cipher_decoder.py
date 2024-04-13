"""
################################################################################
#                                                                              #
# This code was created by veilwr4ith                                          #
#                                                                              #
# Caesar Cipher Decoder                                                        #
#                                                                              #
################################################################################
"""

def caesar_decoder(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text

text = input("Enter the encoded string: ")
shift = int(input("Enter the shift value: "))
decrypted_text = caesar_decoder(text, shift)
print("-" * 30)
print(f"Decrypted text: {decrypted_text}")
