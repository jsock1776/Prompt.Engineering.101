# gpt4_api.py

import requests
from settings import gpt4_api_key
from utils.post_processor import LLMPostProcessor  # Import the new class

def call_gpt4(question):
    headers = {
        "Authorization": f"Bearer {gpt4_api_key}",
        "Content-Type": "application/json"
    }

    # Initial answer to the user’s question
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": question}]
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)

    if response.status_code != 200:
        print("Error generating answer:", response.json())
        return "Error: Could not retrieve response from GPT-4 Mini.", ""

    # Extract content and process with LLMPostProcessor
    try:
        answer = response.json()["choices"][0]["message"]["content"]

        # Generate a follow-up question based on the answer
        follow_up_prompt = f"Given the answer '{answer}', suggest a follow-up question to deepen the user's understanding."
        follow_up_data = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": follow_up_prompt}]
        }
        follow_up_response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=follow_up_data)

        if follow_up_response.status_code != 200:
            print("Error generating follow-up question:", follow_up_response.json())
            follow_up_question = "Error: Could not retrieve follow-up question."
        else:
            follow_up_question = follow_up_response.json()["choices"][0]["message"]["content"]

        # Process the answer and follow-up question
        processor = LLMPostProcessor(answer, follow_up_question)
        processed_answer, processed_follow_up = processor.get_processed_text()

        return processed_answer, processed_follow_up

    except KeyError:
        print("Unexpected response structure:", response.json())
        return "Error: Unexpected response structure from GPT-4 Mini.", ""
