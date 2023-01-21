import base64

def encrypt_base64(text):
    encoded_text = base64.b64encode(text.encode())
    return encoded_text.decode()


def decrypt_base64(encoded_text):
    decoded_text = base64.b64decode(encoded_text.encode()).decode()
    return decoded_text


# Test the function
original_text = "Hello World"
encoded_text = encrypt_base64(original_text)
decoded_text = decrypt_base64(encoded_text)

print(f"Original Text: {original_text}")
print(f"Encoded Text: {encoded_text}")
print(f"Decoded Text: {decoded_text}")