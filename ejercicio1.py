#estructura general del un proyeto de flask
from flask import Flask, render_template
from flask import request 
import math


app=Flask(__name__)

@app.route("/coordenadas")#ruta de acceso de la api, y el tipo de request
def datos():
    return render_template("coordenadas.html")


@app.route("/respuesta", methods=["POST"])#ruta de acceso de la api, y el tipo de request
def respuesta():
    x1=request.form.get("txtX1")
    x2=request.form.get("txtX2") 
    y1=request.form.get("txtY1")
    y2=request.form.get("txtY2") 
    res=math.sqrt(math.pow(int(x2)-int(x1),2)+math.pow(int(y2)-int(y1),2))
    return render_template("respuesta.html",x1=x1, x2=x2, y1=y1, y2=y2,res=res)


if __name__=="__main__":
    app.run(debug=True,port=3000)