"""
################################################################################
#                                                                              #
# This code was created by veilwr4ith                                          #
#                                                                              #
# ROT13 Decoder                                                                #
#                                                                              #
################################################################################
"""

def rot13_decoder(text):
    decoded_text = ""
    for char in text:
        if 'A' <= char <= 'Z':
            decoded_text += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            decoded_text += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            decoded_text += char
    return decoded_text

encoded_text = input("Enter the ROT13 String: ")
decoded_text = rot13_decoder(encoded_text)
print(f"Decoded Text: {decoded_text}")
