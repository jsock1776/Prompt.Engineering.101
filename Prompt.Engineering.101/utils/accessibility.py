import streamlit as st
from gtts import gTTS

def speak_text(text):
    if st.session_state.get("tts_enabled"):
        tts = gTTS(text=text, lang='en')
        tts.save("temp.mp3")
        audio_file = open("temp.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")

def configure_sidebar():
    st.sidebar.header("Accessibility Options")
    st.session_state.text_size = st.sidebar.slider("Adjust Text Size", 12, 24, 16)
    st.session_state.tts_enabled = st.sidebar.checkbox("Enable Text-to-Speech")
    st.session_state.contrast_mode = st.sidebar.checkbox("Enable High Contrast Mode")
