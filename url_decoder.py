"""
################################################################################
#                                                                              #
# This code was created by veilwr4ith                                          #
#                                                                              #
# URL Decoder                                                      #
#                                                                              #
################################################################################
"""

import urllib.parse

def url_decoder():
    encoded_urls = input("Enter the encoded URL(s) separated by comma: ")
    urls = encoded_urls.split(',')
    
    decoded_urls = []
    for encoded_url in urls:
        try:
            decoded_url = urllib.parse.unquote(encoded_url)
            decoded_urls.append(decoded_url)
        except Exception as e:
            print(f"Error decoded URL '{encoded_url.strip()}': {e}")
    
    print("-" * 30)
    print("Decoded URL(s):")
    for decoded_url in decoded_urls:
        print(decoded_url.strip())
    print()

if __name__ == "__main__":
    url_decoder()
