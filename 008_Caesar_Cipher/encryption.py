def encrypt(text, key):
    encrypted_message = ""
    for char in text:
        encrypted_char = int(ord(char)) + key
        encrypted_message += chr(encrypted_char)
    return encrypted_message


def decrypt(text, key):
    decrypted_message = ""
    for char in text:
        decrypted_char = int(ord(char)) - key
        decrypted_message += chr(decrypted_char)
    return decrypted_message
