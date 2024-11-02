import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

# Load environment variables from .env file
load_dotenv()

# Retrieve the encryption key from environment variables
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")
if ENCRYPTION_KEY is None or len(ENCRYPTION_KEY.encode()) != 44:
    raise ValueError("ENCRYPTION_KEY must be a 32-byte Base64-encoded string.")

# Initialize Fernet with the encryption key
cipher_suite = Fernet(ENCRYPTION_KEY)

# Load API keys from environment variables
gpt4_api_key = os.getenv("gpt4_api_key")  # Ensure these names match those in .env
claude_api_key = os.getenv("claude_api_key")
gemini_api_key = os.getenv("gemini_api_key")

print("loaded gpt4 api key")
if gpt4_api_key is None:
    raise ValueError("GPT4_API_KEY is not loaded. Check the .env file and load_dotenv setup.")