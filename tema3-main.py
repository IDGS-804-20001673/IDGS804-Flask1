#estructura general del un proyeto de flask
from flask import Flask  # para importar flask

app=Flask(__name__)

@app.route("/")#ruta de acceso de la api

def index():
    return "!Hola Mundo¡ nuevo msj puto"

#pasamos un strig por parametro en la url
@app.route("/user/<string:user>")
def user(user):
    return "Hola "+ user

#pasamos un int por parametro en la url
@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

#pasamos mas de un parametro en la url
@app.route("/username/<int:id>/<string:username>")
def usern(id,username):
    return "Id:{0} nombre: {1}".format(id,username) 



if __name__=="__main__":
    app.run(debug=True,port=3000)
