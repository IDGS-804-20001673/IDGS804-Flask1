#estructura general del un proyeto de flask
from flask import Flask  # para importar flask
from flask import request #para poner el tipo de request ya sea post o get

app=Flask(__name__)

@app.route("/suma",methods=["GET", "POST"])#ruta de acceso de la api, y el tipo de request
def suma():
    if request.method=="POST" and request.form.get("ope")=="s":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        return "<h1> La suma es: {} </h1>".format(str(int(num1)+int(num2)))
    elif request.method=="POST" and request.form.get("ope")=="r":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        return "<h1> La resta es: {} </h1>".format(str(int(num1)-int(num2)))
    elif request.method=="POST" and request.form.get("ope")=="m":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        return "<h1> La multiplicacion es: {} </h1>".format(str(int(num1)*int(num2)))
    elif request.method=="POST" and request.form.get("ope")=="d":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        return "<h1> La divicion es: {} </h1>".format(str(int(num1)/int(num2)))
    else:
        return''' 
            <form action = "/suma" method="POST">
            <label>N1: </label>
            <input type="text" name="num1"/></br></br>
            <label>N2: </label>
            <input type="text" name="num2"/></br></br>
            <input type="submit" value="Calcular"/>
            <input type="radio" name="ope" value="s" id="s"> <label for="s">Suma</label> <br>
            <input type="radio" name="ope" value="r" id="r"> <label for="r">Resta</label> <br>
            <input type="radio" name="ope" value="m" id="m"> <label for="m">Multiplicacion</label>
            <input type="radio" name="ope" value="d" id="d"> <label for="d">Divicion</label> 
            </form>

    '''



if __name__=="__main__":
    app.run(debug=True,port=3000)
