from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation
# import englishtofrench
# import frenchtoenglish

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return machinetranslation.englishtofrench(textToTranslate)
    #return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    print(request)
    textToTranslate = request.args.get('textToTranslate')
    print(textToTranslate)
    return machinetranslation.frenchtoenglish(textToTranslate)

    # return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # content = get_file('templates/index.html')
    # return Response(content, mimetype="text/html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
