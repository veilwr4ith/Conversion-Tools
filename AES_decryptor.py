"""
################################################################################
#                                                                              #
# This code was created by veilwr4ith                                          #
#                                                                              #
# AES Decryptor                                                                #
#                                                                              #
################################################################################
"""
from Crypto.Cipher import AES
import base64

def decrypt_aes(key, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv=ciphertext[:AES.block_size])
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    pad_length = plaintext[-1]
    plaintext = plaintext[:-pad_length]
    return plaintext.decode('utf-8')

def main():
    key = input("Enter the AES key (16, 24, or 32 bytes): ")
    key_encode = key.encode('utf-8')
    print("Length of key before encoding:", len(key))
    print("Length of key after encoding:", len(key_encode))

    ciphertext_b64 = input("Enter the encoded ciphertext: ")
    ciphertext = base64.b64decode(ciphertext_b64)
    
    try:
        plaintext = decrypt_aes(key_encode, ciphertext)
        print("-" * 30)
        print("Decrypted plaintext:", plaintext)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
