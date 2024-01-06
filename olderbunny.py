from cryptography.fernet import Fernet

# Load the encryption key
with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Read the encrypted text from the file
with open("encrypted.txt", "rb") as file:
    encrypted_text = file.read()

# Decrypt the text
decrypted_text = cipher_suite.decrypt(encrypted_text)
print(decrypted_text.decode())
