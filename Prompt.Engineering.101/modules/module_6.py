import streamlit as st
from llm_apis import gpt4_api, claude_api, gemini_api
import accessibility

def display():
    st.header("Module 6: Advanced Threat Modeling and Ethical Considerations in AI Security")
    
    intro_text = (
        "Dive deeper into advanced threat modeling, using structured frameworks to assess AI security."
        "This module also emphasizes ethical considerations, compliance, and responsible practices in high-stakes applications."	
    )
    st.write(intro_text)
    accessibility.speak_text(intro_text)

    # Dropdown menu to select the LLM
    llm_choice = st.selectbox(
        "Select which AI model you’d like to ask:",
        ("GPT-4", "Claude", "Gemini")
    )

    # Text input for the question
    question = st.text_input("Ask a question about AI techniques, ethics, or compliance relevant to security, accessibility, or adaptive learning:")

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
