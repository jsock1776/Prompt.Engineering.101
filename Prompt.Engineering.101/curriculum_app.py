import streamlit as st
from utils import accessibility, progress  # Import accessibility and progress modules
from modules import (
    module_1, module_2, module_3, module_4, module_5,
    module_6, module_7, module_8, module_9, module_10
)
from llm_apis import gpt4_api, claude_api, gemini_api

# Explicit import if only `configure_sidebar` is needed from accessibility
from utils.accessibility import configure_sidebar

def main():
    # Call configure_sidebar to set up sidebar options
    configure_sidebar()

    st.sidebar.title("AI Curriculum Modules")
    module = st.sidebar.selectbox(
        "Choose the module you'd like to explore:",
        ("Module 1: Foundations of Generative AI and Prompt Engineering",
         "Module 2: Intermediate Prompt Design and Advanced Techniques",
         "Module 3: AI Security Research Fundamentals",
         "Module 4: Integrating AI with DevSecOps",
         "Module 5: Adaptive AI Techniques for Neurodivergent-Friendly Learning",
         "Module 6: Advanced Threat Modeling and Ethical Considerations",
         "Module 7: Large-Scale Threat Modeling and Risk Management",
         "Module 8: Ethical Guardrails and Bias Mitigation in AI",
         "Module 9: High-Performance AI Security Applications",
         "Module 10: Capstone Project – Adaptive AI for Neurodivergent-Friendly Health Interventions")
    )

    # Call the display function for the selected module
    if module == "Module 1: Foundations of Generative AI and Prompt Engineering":
        module_1.display()
    elif module == "Module 2: Intermediate Prompt Design and Advanced Techniques":
        module_2.display()
    elif module == "Module 3: AI Security Research Fundamentals":
        module_3.display()
    elif module == "Module 4: Integrating AI with DevSecOps":
        module_4.display()
    elif module == "Module 5: Adaptive AI Techniques for Neurodivergent-Friendly Learning":
        module_5.display()
    elif module == "Module 6: Advanced Threat Modeling and Ethical Considerations":
        module_6.display()
    elif module == "Module 7: Large-Scale Threat Modeling and Risk Management":
        module_7.display()
    elif module == "Module 8: Ethical Guardrails and Bias Mitigation in AI":
        module_8.display()
    elif module == "Module 9: High-Performance AI Security Applications":
        module_9.display()
    elif module == "Module 10: Capstone Project – Adaptive AI for Neurodivergent-Friendly Health Interventions":
        module_10.display()

if __name__ == "__main__":
    main()
