from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Text to be encrypted
text = "Your encrypted message goes here"

# Encrypt the text
encrypted_text = cipher_suite.encrypt(text.encode())

# Save the encrypted text to a file
with open("encrypted.txt", "wb") as file:
    file.write(encrypted_text)

# Save the encryption key to a file (for later decryption)
with open("key.key", "wb") as key_file:
    key_file.write(key)
 
