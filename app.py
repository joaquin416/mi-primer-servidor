from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "que rollo pa si sirve mi pagina web papi(hazme caso abril)"
