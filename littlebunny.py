from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Text to be encrypted
text = "Hint 2: You've found the next note, as the film moves forward you'll need a boat. Hopefully your hacking skills will keep your afloat."

# Encrypt the text
encrypted_text = cipher_suite.encrypt(text.encode())

# Save the encrypted text to a file
with open("encrypted.txt", "wb") as file:
    file.write(encrypted_text)

# Save the encryption key to a file (for later decryption)
with open("key.key", "wb") as key_file:
    key_file.write(key)
