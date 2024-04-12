"""
################################################################################
#                                                                              #
# This code was created by veilwr4ith                                          #
#                                                                              #
# Unicode Decoder                                                              #
#                                                                              #
################################################################################
"""

def unicode_decoder(text):
    try:
        decoded_text = text.encode('utf-8').decode('unicode-escape')
        return decoded_text
    except UnicodeDecodeError:
        return "Error: Unable to decode Unicode text"

unicode_text = input("Enter the Unicode Text: ")
decoded_text = unicode_decoder(unicode_text)
print("Decoded text:", decoded_text)
