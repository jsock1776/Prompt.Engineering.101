import google.generativeai as genai
import os
from utils.post_processor import LLMPostProcessor

# Configure the API key once when the module is imported
genai.configure(api_key=os.environ["gemini_api_key"])  # Store API key securely in environment variables

def call_gemini(question):
    try:
        # Initialize the Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Generate content based on the user's question
        response = model.generate_content(question)
        answer = response.text  # Store the generated answer text

        # Generate a follow-up question based on the initial answer
        follow_up_prompt = f"Based on the answer '{answer}', suggest a follow-up question to ask the user."
        follow_up_response = model.generate_content(follow_up_prompt)
        follow_up_question = follow_up_response.text  # Store the follow-up question text

       # Process the answer and follow-up question
        processor = LLMPostProcessor(answer, follow_up_question)
        processed_answer, processed_follow_up = processor.get_processed_text()

        return processed_answer, processed_follow_up

    except Exception as e:
        print("Error generating content with Gemini:", e)
        return "Error: Failed to generate content with Gemini.", ""
