"""
################################################################################
#                                                                              #
# This code was created by veilwr4ith                                          #
#                                                                              #
# Base 16, 32, 64 Decoder                                                      #
#                                                                              #
################################################################################
"""

import base64

def base16_decode(encoded_text):
    try:
        decoded_bytes = bytes.fromhex(encoded_text)
        decoded_text = decoded_bytes.decode('utf-8')
        print(f"Decoded String: {decoded_text}")
    except:
        print("Decoding Failed.")
def base64_decode(encoded_text):
    try:
        decoded_bytes = base64.b64decode(encoded_text)
        decoded_text = decoded_bytes.decode('utf-8')
        print(f"Decoded String: {decoded_text}")
    except:
        print("Decoding Failed.")

def base32_decode(encoded_text):
    try:
        decoded_bytes = base64.b32decode(encoded_text)
        decoded_text = decoded_bytes.decode('utf-8')
        print(f"Decoded String: {decoded_text}")
    except:
        print("Decoding Failed.")

option = int(input("Choose if Base16, Base32, Base64:\n1. Base16\n2. Base32\n3. Base64\nPlease select a number: "))

if option == 1:
    encoded_string = input("Enter the Encoded String: ")
    print("-" * 30)
    base16_decode(encoded_string)
elif option == 2:
    encoded_string = input("Enter the Encoded String: ")
    print("-" * 30)
    base32_decode(encoded_string)
elif option == 3:
    encoded_string = input("Enter the Encoded String: ")
    print("-" * 30)
    base64_decode(encoded_string)
else:
    print("inavlid Option.")
