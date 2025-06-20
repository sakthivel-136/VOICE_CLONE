import streamlit as st
from gtts import gTTS
import uuid

st.set_page_config(page_title="Text to Speech", layout="centered")
st.title("🗣️ Text to Speech (gTTS Version)")
st.write("Enter text and select a voice (simulated), then listen to the result.")

# Fake voice options
voice_samples = ["Dhoni", "Vijay", "Trump"]
selected_voice = st.radio("🎤 Select a voice:", voice_samples)

text_input = st.text_area("📝 Enter the text to synthesize")

if st.button("🔁 Clone Voice"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        tts = gTTS(text_input)
        output_file = f"output_{uuid.uuid4().hex}.mp3"
        tts.save(output_file)

        st.success(f"✅ Cloned using simulated voice: {selected_voice}")
        st.audio(output_file, format="audio/mp3")
        with open(output_file, "rb") as f:
            st.download_button("⬇️ Download Audio", f, file_name="voice.mp3")
