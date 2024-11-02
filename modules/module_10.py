import streamlit as st
from llm_apis import gpt4_api, claude_api, gemini_api
from utils import accessibility

def display():
    st.header("Module 10: Capstone Project – Adaptive AI for Neurodivergent-Friendly Health Interventions")
    
    intro_text = (
        "In this capstone project, you’ll develop an adaptive AI model for neurodivergent-friendly health interventions, "
        "integrating real-time bias mitigation, compliance with healthcare regulations, and patient-centric design."
    )
    st.write(intro_text)
    accessibility.speak_text(intro_text)

    # Dropdown to select the LLM
    llm_choice = st.selectbox(
        "Choose the AI model you'd like to consult for the Capstone Project:",
        ("GPT-4", "Claude", "Gemini")
    )

    # Single question input relevant to Module 10's focus
    question = st.text_input("Ask a question about adaptive AI, bias mitigation, or healthcare compliance:")

    # Process the question based on the selected LLM
    if question:
        if llm_choice == "GPT-4":
            answer = gpt4_api.call_gpt4(question)
            st.write(f"**GPT-4 Response:** {answer}")
        elif llm_choice == "Claude":
            answer = claude_api.call_claude(question)
            st.write(f"**Claude Response:** {answer}")
        elif llm_choice == "Gemini":
            answer = gemini_api.call_gemini(question)
            st.write(f"**Gemini Response:** {answer}")
