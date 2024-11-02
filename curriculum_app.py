import streamlit as st
from utils import accessibility, progress  # Import accessibility and progress modules
from modules import (
    module_1, module_2, module_3, module_4, module_5,
    module_6, module_7, module_8, module_9, module_10
)
from llm_apis import gpt4_api, claude_api, gemini_api
from llm_apis.gpt4_api import call_gpt4
from llm_apis.claude_api import call_claude
from llm_apis.gemini_api import call_gemini
from utils.accessibility import configure_sidebar
import re

# Define the dictionary with module headers and intro texts for all 10 modules
module_info = {
    "Module 1": ("Foundations of Generative AI and Prompt Engineering", "This module introduces you to the fundamentals of generative AI and prompt engineering..."),
    "Module 2": ("Intermediate Prompt Design and Advanced Techniques", "Building on foundational skills, this module covers advanced techniques in prompt engineering..."),
    "Module 3": ("AI Security Research Fundamentals", "Explore the integration of AI in security through threat intelligence and vulnerability detection..."),
    "Module 4": ("Integrating AI with DevSecOps", "Learn the principles of DevSecOps and how AI can assist in secure development and automation..."),
    "Module 5": ("Adaptive AI Techniques for Neurodivergent-Friendly Learning", "This module focuses on adaptive AI techniques tailored for cognitive accessibility and neurodivergent learners..."),
    "Module 6": ("Advanced Threat Modeling and Ethical Considerations", "Delve into advanced threat modeling frameworks and ethical considerations in AI-driven security..."),
    "Module 7": ("Large-Scale Threat Modeling and Risk Management", "Understand high-impact threat identification and scalable threat modeling frameworks for large systems..."),
    "Module 8": ("Ethical Guardrails and Bias Mitigation in AI", "Explore the development of ethical frameworks and guardrails in AI, including bias detection and mitigation..."),
    "Module 9": ("High-Performance AI Security Applications", "Focus on optimization of AI models for high-stakes applications and anomaly detection in security..."),
    "Module 10": ("Capstone Project – Adaptive AI for Neurodivergent-Friendly Health Interventions", "Develop a capstone project that combines adaptive AI techniques with healthcare applications...")
}

# Formatting functions for each LLM
def format_claude_text(text):
    if isinstance(text, tuple):
        text = ' '.join(text)
    text = text.replace("\\n", "\n").replace("\\r", "\n").strip()
    text = re.sub(r'(\n|^)\s*[-*•]\s+', '\n', text)  # Remove unnecessary bullets
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Remove bold markers
    text = re.sub(r'\n?(\d+)\.\s+', r'\n\n\1. ', text)  # Standardize numbered lists
    return text.strip()

def format_gpt4_text(text):
    if isinstance(text, tuple):
        text = ' '.join(text)
    text = text.replace("\\n", "\n").replace("\\r", "\n").strip()
    text = re.sub(r'(\n|^)\s*[-*•]\s+', '\n', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Remove bold formatting entirely
    text = re.sub(r'\n?(\d+)\.\s+', r'\n\n\1. ', text)
    return text.strip()

def format_gemini_text(text):
    if isinstance(text, tuple):
        text = ' '.join(text)
    
    # Standardize line breaks and remove redundant escape characters
    text = text.replace("\\n", "\n").replace("\\r", "\n").strip()
    
    # Remove any bullet symbols, list markers, or extra symbols
    text = re.sub(r'(\n|^)\s*[-*•]\s+', '\n', text)  # Remove all bullet points

    # Normalize numbered lists to ensure each section is clearly separated
    text = re.sub(r'\n?(\d+)\.\s+', r'\n\n\1. ', text)  # Double newlines after numbered items

    # Remove any bold markers like ** or __ to keep plain text
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)

    # Remove any excessive newlines for clean, consistent spacing
    text = re.sub(r'\n{2,}', '\n\n', text)

    # Final strip to ensure no trailing/leading whitespace
    return text.strip()

# Function to display LLM response with proper formatting and follow-up question
def display_llm_response(model_choice, main_answer, follow_up_question):
    if model_choice == "Claude":
        formatted_answer = format_claude_text(main_answer)
    elif model_choice == "GPT-4":
        formatted_answer = format_gpt4_text(main_answer)
    elif model_choice == "Gemini":
        formatted_answer = format_gemini_text(main_answer)
    else:
        formatted_answer = main_answer  # Default to raw answer if model is unknown

    # Display the main response
    st.write(formatted_answer)

    # Display the follow-up question
    if follow_up_question:
        st.markdown("**Follow-Up Question:**")
        st.write(follow_up_question.strip())

# Updated call functions to simulate follow-up question generation
def call_gpt4(question):
    main_response = gpt4_api.call_gpt4(question)
    follow_up_question = "What further insights would you like to explore on this topic?"
    return main_response, follow_up_question

def call_claude(question):
    main_response = claude_api.call_claude(question)
    follow_up_question = "Is there a specific area within this topic you're interested in?"
    return main_response, follow_up_question

def call_gemini(question):
    main_response = gemini_api.call_gemini(question)
    follow_up_question = "Would you like more examples or a deeper explanation on this topic?"
    return main_response, follow_up_question

# Display function for each module
def display_module(module_name):
    title, intro_text = module_info[module_name]
    st.header(title)
    st.write(intro_text)
    accessibility.speak_text(intro_text)

    llm_choice = st.selectbox(
        "Select which AI model you’d like to ask:",
        ("GPT-4", "Claude", "Gemini")
    )

    question = st.text_input("Ask a question about the module's topic:")

    if question:
        if llm_choice == "GPT-4":
            main_answer, follow_up_question = call_gpt4(question)
            display_llm_response("GPT-4", main_answer, follow_up_question)
        elif llm_choice == "Claude":
            main_answer, follow_up_question = call_claude(question)
            display_llm_response("Claude", main_answer, follow_up_question)
        elif llm_choice == "Gemini":
            main_answer, follow_up_question = call_gemini(question)
            display_llm_response("Gemini", main_answer, follow_up_question)

# Main app interface
def main():
    configure_sidebar()
    st.sidebar.title("AI Curriculum Modules")
    module = st.sidebar.selectbox(
        "Choose the module you'd like to explore:",
        [f"Module {i}" for i in range(1, 11)]
    )
    display_module(module)

if __name__ == "__main__":
    main()
