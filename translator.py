from googletrans import Translator

translator = Translator()

def detect_language(text):
    return translator.detect(text).lang

def translate_text(text, target_lang):
    return translator.translate(text, dest=target_lang).text