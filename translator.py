from langdetect import detect
from deep_translator import GoogleTranslator

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"

def translate_text(text, target_lang):
    try:
        return GoogleTranslator(
            source='auto',
            target=target_lang
        ).translate(text)
    except Exception as e:
        return f"Translation Error: {str(e)}"