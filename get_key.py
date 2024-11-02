from cryptography.fernet import Fernet

# This will generate a valid 32-byte Base64-encoded encryption key
print(Fernet.generate_key().decode())  # Output will look like "PG--DbcCxV878dBUIz6YP_2aV6UdjLBHvKBA71k5iio="
