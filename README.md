# 🤖 AI Powered Text Summarizer & Language Translator

An AI-powered web application that summarizes lengthy text and translates content into multiple languages using Natural Language Processing (NLP) techniques. Built with Python, Streamlit, NLTK, and Deep Translator.

---

## 📌 Features

* ✨ Extractive Text Summarization using TF-IDF
* 🌍 Multi-language Translation Support
* 🔍 Automatic Language Detection
* 📝 Generate concise summaries from long text
* 🎯 User-friendly and responsive web interface
* 🌐 Supports multiple languages including:

  * English
  * Hindi
  * Telugu
  * Tamil
  * Kannada
  * Malayalam
  * Urdu
  * Bengali
  * Chinese
  * Japanese
  * Russian
  * French

---

## 🛠️ Technologies Used

* Python
* Streamlit
* NLTK
* Scikit-learn
* NumPy
* LangDetect
* Deep Translator

---

## 📂 Project Structure

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

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Text-Summarizer-and-Language-Translator.git
cd Text-Summarizer-and-Language-Translator
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 📖 How It Works

### Text Summarization

1. User enters text.
2. Language is automatically detected.
3. Text is processed using TF-IDF based extractive summarization.
4. A concise summary is generated.
5. Summary can be translated into the selected language.

### Language Translation

1. User enters text.
2. Selects the target language.
3. The application translates the text using Deep Translator.
4. Translated output is displayed instantly.

---

## 🎯 Use Cases

- Students summarizing study materials
- Researchers analyzing long documents
- Content creators generating quick summaries
- Language learners translating text
- Professionals handling multilingual content

---

## 🔮 Future Enhancements

- PDF Upload and Summarization
- AI-based Abstractive Summarization
- Voice Input Support
- Text-to-Speech Conversion
- Download Results as PDF
- Dark Mode Support

---

## 🚀 Live Demo

🔗 https://text-summarizer-and-language-translator.streamlit.app/

---

## 👨‍💻 Author

**Md Jahangeer**

B.Tech (Computer Science & Engineering)

Python Developer | AI & Machine Learning Enthusiast

GitHub: https://github.com/Jahangeer4002

---

## 📄 License

This project is developed for educational and learning purposes.
