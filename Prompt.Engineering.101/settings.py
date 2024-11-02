import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

# Load .env file for local development
load_dotenv()

# Load encryption key from environment
ENCRYPTION_KEY = os.getenv("encryption_key")
cipher_suite = Fernet(ENCRYPTION_KEY.encode())


# Load API keys from environment variables
gpt4_api_key = os.getenv("gpt4_api_key")
claud_api_key = os.getenv("claud_api_key")
gemini_api_key = os.getenv("gemini_api_key")

# Encryption key for secure data storage (store this securely in production)
ENCRYPTION_KEY = os.getenv("encryption_key", Fernet.generate_key())  # Fallback to a generated key if not set





