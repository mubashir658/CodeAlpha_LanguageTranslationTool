import streamlit as st
from deep_translator import MyMemoryTranslator
from gtts import gTTS
import io

# Page configuration
st.set_page_config(page_title="Language Translation Tool", page_icon="🌐", layout="centered")

st.title("🌐 Language Translation Tool")
st.write("Translate text across languages with audio speech support.")

# Mapping: Display Name -> (MyMemory Code, gTTS Code)
LANGUAGES = {
    "English": ("en-GB", "en"),
    "Spanish": ("es-ES", "es"),
    "French": ("fr-FR", "fr"),
    "German": ("de-DE", "de"),
    "Hindi": ("hi-IN", "hi"),
    "Urdu": ("ur-PK", "ur"),
    "Arabic": ("ar-SA", "ar"),
    "Portuguese": ("pt-PT", "pt"),
    "Italian": ("it-IT", "it"),
    "Japanese": ("ja-JP", "ja")
}

lang_names = list(LANGUAGES.keys())

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Source Language", options=lang_names, index=0)
with col2:
    target_lang = st.selectbox("Target Language", options=lang_names, index=1)

input_text = st.text_area("Enter text to translate:", height=130, placeholder="Type your text here (under 500 characters)...")

if st.button("Translate", type="primary"):
    if not input_text.strip():
        st.warning("Please enter some text to translate.")
    elif len(input_text) > 500:
        st.warning(f"Text is too long ({len(input_text)} characters). Please keep it under 500 characters.")
    elif source_lang == target_lang:
        st.info("Source and target languages are the same.")
        st.subheader("Translated Text:")
        st.code(input_text, language=None)
    else:
        try:
            src_code, _ = LANGUAGES[source_lang]
            tgt_code, tts_lang = LANGUAGES[target_lang]

            # Translation
            translated_result = MyMemoryTranslator(source=src_code, target=tgt_code).translate(input_text)

            st.success("Translation Successful!")
            st.subheader("Translated Text:")
            # Displays in a copyable code-block box
            st.code(translated_result, language=None)

            # Audio Speech Generation
            tts = gTTS(text=translated_result, lang=tts_lang)
            audio_buffer = io.BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)

            st.write("🔊 Listen to translation:")
            st.audio(audio_buffer, format="audio/mp3")

        except Exception as e:
            st.error(f"Translation failed: {e}")