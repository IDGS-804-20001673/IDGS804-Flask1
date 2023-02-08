#estructura general del un proyeto de flask
from flask import Flask, render_template
from flask import request 
import math


app=Flask(__name__)

@app.route("/")#ruta de acceso de la api, y el tipo de request
def datos():
    return render_template("cine.html")


@app.route("/resultadoCine", methods=["POST"])#ruta de acceso de la api, y el tipo de request
def resultadoCine():
    nombre=request.form.get("txtNom")
    compradores=request.form.get("txtCompradores") 
    tarjeta=request.form.get("tarjeta")
    boletas=request.form.get("txtBoletas") 

    if int(boletas) > int(compradores)*7:
         res="No se pudo procesar la compra la cantidad de boletas por persona debe ser menor a 7"
    else:
        res=int(boletas)*12
        if int(boletas) > 5:
            res=res*.85
        elif int(boletas) == 3 or int(boletas) == 4 or int(boletas) == 5:
            res=res*.90
        else:
            res = res 
        
        if tarjeta == "si":
            res=res*.90

    return render_template("resultadoCine.html",nombre=nombre, compradores=compradores, boletas=boletas, res=res)


if __name__=="__main__":
    app.run(debug=True,port=3000)