import streamlit as st
from TTS.api import TTS
import os
import uuid

# ✅ Load the multilingual YourTTS model once
@st.cache_resource
def load_tts_model():
    return TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False)

tts = load_tts_model()

# ✅ Streamlit page setup
st.set_page_config(page_title="Text to Speech", layout="centered")
st.markdown("<h1 style='text-align: center;'>🗣️ Text to Speech (Voice Cloner)</h1>", unsafe_allow_html=True)
st.write("Enter text and select a voice to hear the cloned output.")

# ✅ Friendly names to audio files
voice_samples = {
    "Dhoni": "MSD_VOICE.wav",
    "Vijay": "Vijay_voice.wav",
    "Trump": "Trump_voice.wav"
}

# ✅ Voice selection UI
selected_voice_display = st.radio("🎤 Select a voice:", list(voice_samples.keys()))
selected_voice_file = voice_samples[selected_voice_display]

# ✅ Text input
text_input = st.text_area("📝 Enter the text to clone", height=100)

# ✅ Clone button
if st.button("🔁 Clone Voice"):
    if text_input.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        output_filename = f"cloned_{uuid.uuid4().hex}.wav"

        # ✅ Clone the voice
        tts.tts_to_file(
            text=text_input,
            speaker_wav=selected_voice_file,
            file_path=output_filename,
            language='en'
        )

        st.success("✅ Cloning successful!")

        # ✅ Play audio
        st.audio(output_filename, format="audio/wav")

        # ✅ Download button
        with open(output_filename, "rb") as audio_file:
            st.download_button(
                label="⬇️ Download Cloned Audio",
                data=audio_file,
                file_name="cloned_voice.wav",
                mime="audio/wav"
            )
