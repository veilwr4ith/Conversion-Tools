import base64

def decode_ascii85(encoded_data):
    try:
        decoded_data = base64.a85decode(encoded_data.encode('ascii'))
        return decoded_data.decode('utf-8')
    except base64.binascii.Error:
        return "Error: Invalid ASCII85 encoded data"  
      
encoded_data = input("Enter the encoded data: ")
decoded_data = decode_ascii85(encoded_data)
print(f"Decoded String: {decoded_data}")