#estructura general del un proyeto de flask
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/datos")#ruta de acceso de la api, y el tipo de request
def datos():
    nombre="Amanda"
    lista1="uno", "dos", "tres", "cuatro"
    return render_template("datos.html", nombre=nombre, lista1=lista1)


if __name__=="__main__":
    app.run(debug=True,port=3000)