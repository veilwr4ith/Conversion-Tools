import quopri

def quoted_printable_decoder(text):
    try:
        decoded_text = quopri.decodestring(text).decode('utf-8')
        return decoded_text
    except Exception as fuck:
        print("Error: ", fuck)

quoted_printable_text = input("Enter the QPT: ")
decoded_text = quoted_printable_decoder(quoted_printable_text)
print(f"Decoded Text: {decoded_text}")