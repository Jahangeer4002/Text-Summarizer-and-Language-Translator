# AI Powered Text Summarizer & Language Translator

## Overview

AI Powered Text Summarizer & Language Translator is a web-based NLP application developed using Python and Streamlit. The application helps users generate concise summaries from lengthy text and translate content into multiple languages. It combines Natural Language Processing (NLP) techniques with language translation capabilities to improve content accessibility and understanding.

## Features

* Text Summarization using TF-IDF based Extractive Summarization
* Multi-language Text Translation
* Automatic Language Detection
* Interactive and User-Friendly Web Interface
* Support for Multiple Languages including English, Hindi, Telugu, Tamil, Kannada, Malayalam, Urdu, Bengali, Chinese, Japanese, Russian, and French
* Real-time Processing and Results

## Technologies Used

* Python
* Streamlit
* NLTK
* Scikit-learn
* NumPy
* LangDetect
* Deep Translator

## Project Structure

```text
Text-Summarizer-and-Language-Translator
│
├── app.py
├── summarizer.py
├── translator.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit
    └── config.toml
```

## Installation

### Clone Repository

```bash
git clone https://github.com/Jahangeer4002/Text-Summarizer-and-Language-Translator.git
cd Text-Summarizer-and-Language-Translator
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## How It Works

### Text Summarization

1. User enters text.
2. The system detects the language.
3. Text is translated to English if necessary.
4. TF-IDF based extractive summarization is applied.
5. Summary is translated back to the selected language.

### Language Translation

1. User enters text.
2. Selects the target language.
3. The application translates the content using Deep Translator.
4. The translated text is displayed instantly.

## Future Enhancements

* PDF Document Upload and Summarization
* Voice Input Support
* AI-based Abstractive Summarization
* Text-to-Speech Functionality
* Dark Mode Support
* Download Summary and Translation as PDF

## Deployment

The application is deployed using Streamlit Community Cloud.

## Author

Md Jahangeer

Python Developer | AI & Machine Learning Enthusiast

## License

This project is developed for educational and learning purposes.
