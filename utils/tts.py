from gtts import gTTS

def text_to_speech(text, filename="static/output.mp3", lang='ta'):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    return filename
