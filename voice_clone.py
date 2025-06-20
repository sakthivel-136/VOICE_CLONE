import streamlit as st
from gtts import gTTS
import uuid
import os

# ✅ Page setup
st.set_page_config(page_title="Text to Speech", layout="centered")
st.title("🗣️ Text to Speech (Online-Friendly)")
st.write("Enter text and select a voice style (simulated), then hear the output.")

# ✅ Fake voice styles
voice_styles = {
    "Dhoni": "en",
    "Vijay": "en",
    "Trump": "en"
}

# ✅ Select voice (simulated)
selected_voice = st.radio("🎤 Choose a Voice Style:", list(voice_styles.keys()))
text_input = st.text_area("📝 Enter text to synthesize", height=100)

# ✅ Clone button
if st.button("🔁 Generate Voice"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        lang = voice_styles[selected_voice]
        tts = gTTS(text_input, lang=lang)
        output_file = f"output_{uuid.uuid4().hex}.mp3"
        tts.save(output_file)

        st.success(f"✅ Voice generated as '{selected_voice}' style.")
        st.audio(output_file)

        with open(output_file, "rb") as f:
            st.download_button("⬇️ Download Audio", f, file_name="output.mp3")

        os.remove(output_file)
