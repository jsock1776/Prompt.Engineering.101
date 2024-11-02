import requests
from settings import gemini_api_key
# Gemini 1.5 Flash API call
def call_gemini(prompt):
    response = requests.post(
        "https://api.google.com/v1/engines/gemini-1.5/completions",  # Hypothetical endpoint
        headers={"Authorization": f"Bearer {gemini_api_key}"},
        json={"prompt": prompt, "max_tokens": 100}
    )
    return response.json()["choices"][0]["text"]