import idna

def punnycode_decoder(text):
    try:
        decoded_text = idna.decode(text)
        return decoded_text
    except idna.IDNAError as e:
        print(f"Error: {e}")
        return None

punnycode_text = input("Enter the Punnycode Text: ")
decoded_text = punnycode_decoder(punnycode_text)
print(f"Decoded Punnycode Text: {decoded_text}")