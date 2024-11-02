import requests
from settings import claude_api_key
from utils.post_processor import LLMPostProcessor  # Import the LLMPostProcessor

def call_claude(question):
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "accept": "application/json",
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
        "x-api-key": claude_api_key
    }
    data = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_json = response.json()

        # Validate response structure and extract text content
        if "content" in response_json and isinstance(response_json["content"], list) and "text" in response_json["content"][0]:
            main_answer = response_json["content"][0]["text"]
            follow_up_question = "What other aspects of this topic would you like to explore?"  # Generic follow-up

            # Process answer and follow-up question with LLMPostProcessor
            processor = LLMPostProcessor(main_answer, follow_up_question)
            processed_answer, processed_follow_up = processor.get_processed_text()

            return processed_answer, processed_follow_up
        else:
            return "Error: Unexpected response structure from Claude API.", ""
    else:
        print("API Error:", response.status_code, response.text)
        return f"Error: API returned status code {response.status_code}", ""
