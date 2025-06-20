import streamlit as st
from gtts import gTTS
import uuid
import os

st.set_page_config(page_title="Text to Speech", layout="centered")
st.title("🗣️ Text to Speech (Online)")

voices = {
    "Dhoni": "en",
    "Vijay": "en",
    "Trump": "en"
}

selected_voice = st.radio("🎤 Select a Voice", list(voices.keys()))
text = st.text_area("📝 Enter Text to Speak")

if st.button("🔁 Generate Voice"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        tts = gTTS(text, lang=voices[selected_voice])
        filename = f"{uuid.uuid4().hex}.mp3"
        tts.save(filename)

        st.success(f"✅ Generated using {selected_voice}")
        st.audio(filename)

        with open(filename, "rb") as f:
            st.download_button("⬇️ Download", f, file_name="voice.mp3")

        os.remove(filename)
