from cryptography.fernet import Fernet

# Generate a new encryption key
encryption_key = Fernet.generate_key()

# Display the key to copy manually
print("Your Encryption Key:", encryption_key.decode())
