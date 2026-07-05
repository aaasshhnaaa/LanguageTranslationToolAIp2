import streamlit as st
from deep_translator import GoogleTranslator

# PAGE CONFIGURATION
st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# TITLE
st.title("🌍 AI Language Translation Tool")
st.write("Translate text between multiple languages using Google's Translation API.")

# LANGUAGE DICTIONARY
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Punjabi": "pa",
    "Italian": "it",
    "Russian": "ru",
    "Arabic": "ar"
}

# SOURCE LANGUAGE
source_language = st.selectbox(
    "Select Source Language",
    list(languages.keys())
)

# TARGET LANGUAGE
target_language = st.selectbox(
    "Select Target Language",
    list(languages.keys()),
    index=1
)

# INPUT TEXT
text = st.text_area(
    "Enter Text to Translate",
    height=180,
    placeholder="Type your text here..."
)

# TRANSLATE BUTTON
if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        translator = GoogleTranslator(
            source=languages[source_language],
            target=languages[target_language]
        )

        translated_text = translator.translate(text)

        st.success("Translation Successful!")

        st.text_area(
            "Translated Text",
            translated_text,
            height=180
        )
