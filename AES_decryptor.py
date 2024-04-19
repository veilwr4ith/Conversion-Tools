from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def decrypt_aes(key, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv=ciphertext[:AES.block_size])
    plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
    return plaintext.decode('utf-8')

def main():
    key = input("Enter the AES key (16, 24, or 32 bytes): ").encode('utf-8')
    ciphertext_b64 = input("Enter the encoded ciphertext: ")
    ciphertext = base64.b64decode(ciphertext_b64)
    
    try:
        plaintext = decrypt_aes(key, ciphertext)
        print("-" * 30)
        print("Decrypted plaintext:", plaintext)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
