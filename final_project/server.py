from machinetranslation import translator
from flask import Flask, render_template, request
import json
print('2')
app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french_text = translator.englishToFrench(textToTranslate)
    return french_text, "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_text = translator.frenchToEnglish(textToTranslate)
    return english_text, "Translated text to English"

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

print('1')
