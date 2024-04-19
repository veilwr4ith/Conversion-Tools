from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def decrypt_rsa(private_key, ciphertext_b64):
    private_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    ciphertext = base64.b64decode(ciphertext_b64)
    plaintext = cipher_rsa.decrypt(ciphertext)
    return plaintext.decode('utf-8')

def main():
    private_key_str = input("Enter the RSA private key: ")
    ciphertext_b64 = input("Enter the encoded ciphertext: ")
    
    try:
        plaintext = decrypt_rsa(private_key_str, ciphertext_b64)
        print("-" * 30)
        print("Decrypted plaintext:", plaintext)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
