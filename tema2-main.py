#estructura general del un proyeto de flask
from flask import Flask  # para importar flask

app=Flask(__name__)

@app.route("/")#ruta de acceso de la api

def index():
    return "!Hola Mundo¡ nuevo msj puto"

@app.route("/hola")
def hola():
    return "Hola IDGS804"

if __name__=="__main__":
    app.run(debug=True,port=3000)
