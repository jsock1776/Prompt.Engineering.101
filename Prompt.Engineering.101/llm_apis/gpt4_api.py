import requests
from settings import gpt4_api_key

# GPT-4 API call

def call_gpt4(prompt):
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci-codex/completions",
        headers={"Authorization": f"Bearer {gpt4_api_key}"},
        json={"prompt": prompt, "max_tokens": 100}
    )
    return response.json()["choices"][0]["text"]