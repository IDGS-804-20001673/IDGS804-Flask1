#estructura general del un proyeto de flask
from flask import Flask  # para importar flask

app=Flask(__name__)

@app.route("/")#ruta de acceso de la api

def index():
    return "!Hola Mundo¡ nuevo msj puto"


if __name__=="__main__":
    app.run(debug=True,port=3000)

