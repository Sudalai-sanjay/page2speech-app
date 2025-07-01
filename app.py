from flask import Flask, render_template, request, send_file
import os
from utils.extract_text import extract_text_from_pdf
from utils.translate_text import translate_text
from utils.tts import text_to_speech

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["pdf"]
        lang = request.form["language"]
        
        # Save uploaded file
        file_path = os.path.join("static", "input.pdf")
        file.save(file_path)

        # Extract text, translate, convert to audio
        text = extract_text_from_pdf(file_path)
        translated_text = translate_text(text, lang)
        audio_file = text_to_speech(translated_text, lang=lang)

        return render_template("index.html", audio=audio_file)

    return render_template("index.html", audio=None)

if __name__ == "__main__":
    app.run(debug=True)
