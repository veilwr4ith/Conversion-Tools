"""
################################################################################
#                                                                              #
# This code was created by veilwr4ith                                          #
#                                                                              #
# Hex Decoder                                                                  #
#                                                                              #
################################################################################
"""

def hex_to_plaintext(hex_string):
    try:
        hex_string = hex_string.replace(" ", "")
        byte_data = bytes.fromhex(hex_string)
        plaintext = byte_data.decode('utf-8')
        return plaintext
    except Exception as i:
        print("Error:", i)
        return None
    
hex_input = input("Enter the hexadecimal string: ")

plaintext = hex_to_plaintext(hex_input)
if plaintext:
    print("Plaintext:", plaintext)
else:
    print("Failed to decode the hex string.")
