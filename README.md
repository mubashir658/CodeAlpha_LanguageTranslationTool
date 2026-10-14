# 🌐 CodeAlpha Language Translation Tool

A clean and user-friendly language translation web app built with Streamlit. It lets users translate text between multiple languages and listen to the translated result using text-to-speech.

This project was created as part of the CodeAlpha Artificial Intelligence Internship.

## ✨ Features

- Translate text across multiple global languages
- Simple and modern Streamlit interface
- Language selection for source and target text
- Instant translated output preview
- Audio playback for translated text with gTTS
- Copy-friendly output display for easy sharing

## 🧩 Tech Stack

- Python
- Streamlit
- deep-translator (MyMemory)
- gTTS (Google Text-to-Speech)

## 🚀 Quick Start

### 1) Clone the repository

```bash
git clone https://github.com/mubashir658/CodeAlpha_LanguageTranslationTool.git
cd CodeAlpha_LanguageTranslationTool
```

### 2) Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run the app

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (usually `http://localhost:8501`).

## 📖 How It Works

1. Choose the source language and target language.
2. Enter text in the text box.
3. Click the Translate button.
4. View the translated text instantly.
5. Listen to the translated output with the built-in audio player.

## 📁 Project Structure

```text
CodeAlpha_LanguageTranslationTool/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules
└── venv/                   # Virtual environment (local)
```

## 🛠️ Example Languages Supported

- English
- Spanish
- French
- German
- Hindi
- Urdu
- Arabic
- Portuguese
- Italian
- Japanese

## ⚠️ Notes

- Text input is limited to 500 characters in this app.
- Translation quality depends on the selected language pair and external translation service availability.

## 📄 License

This project is provided for educational and personal use.

## 🙌 Author

Built with Python and Streamlit for a simple, accessible translation experience.