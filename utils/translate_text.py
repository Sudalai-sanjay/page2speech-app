from deep_translator import GoogleTranslator

def translate_text(text, dest_lang='ta'):
    try:
        result = GoogleTranslator(source='auto', target=dest_lang).translate(text)
        return result
    except Exception as e:
        print("Translation Error:", e)
        return "Translation failed"
