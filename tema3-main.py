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
@app.route("/usernamçe/<int:id>/<string:username>")
def usern(id,username):
    return "Id:{0} nombre: {1}".format(id,username) 


#pasamos mas de un parametro en la url
@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma es {}".format(n1+n2) 



if __name__=="__main__":
    app.run(debug=True,port=3000)
