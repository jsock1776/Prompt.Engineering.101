import requests
from settings import claud_api_key
# Claude API call
def call_claude(prompt):
    response = requests.post(
        "https://api.anthropic.com/v1/engines/claude/completions",
        headers={"Authorization": f"Bearer {claud_api_key}"},
        json={"prompt": prompt, "max_tokens": 100}
    )
    return response.json()["choices"][0]["text"]