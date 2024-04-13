"""
################################################################################
#                                                                              #
# This code was created by veilwr4ith                                          #
#                                                                              #
# UNIX Datetime Decoder                                                        #
#                                                                              #
################################################################################
"""

import datetime

def unix_time_decoder(timestamp):
    try:
        timestamp = int(timestamp)
        date_time = datetime.datetime.utcfromtimestamp(timestamp)
        return date_time.strftime('%Y-%m-%d %H:%M:%S UTC')
    except ValueError:
        return "Invalid Unix timestamp"

timestamp = input("Enter Unix timestamp: ")
decoded_time = unix_time_decoder(timestamp)
print("-" * 30)
print("Decoded time:", decoded_time)
