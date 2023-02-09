#estructura general del un proyeto de flask
from flask import Flask, render_template
from flask import request 
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta


app=Flask(__name__)

@app.route("/")#ruta de acceso de la api, y el tipo de request
def datos():
    return render_template("examenPrueba.html")


@app.route("/examenPruebaRespuesta", methods=["POST"])#ruta de acceso de la api, y el tipo de request
def examenPruebaRespuesta():
    nombre=request.form.get("txtNom")
    apa=request.form.get("txtAPaterno") 
    ama=request.form.get("txtAMaterno")

    dia=request.form.get("txtDia")
    mes=request.form.get("txtMes") 
    año=request.form.get("txtAnno") 

    edad=relativedelta(datetime.now(), datetime(int(año), int(mes), int(dia)))
    edad=edad.years+1

    
    p1=request.form.get("txt1")
    p2=request.form.get("txt2") 
    p3=request.form.get("txt3") 
    p4=request.form.get("txt4") 
    p5=request.form.get("txt5") 
    
   
    if int(año) == 1912 or int(año) == 1924 or int(año) == 1936 or int(año) == 1948 or int(año) == 1960 or int(año) == 1972 or int(año) == 1984 or int(año) == 1996 or int(año) == 2008 or int(año) == 2020 :
         zodiacal="Rata"
         image="http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Rata-300x257.jpg"
    elif int(año) == 1913 or int(año) == 1925 or int(año) == 1937 or int(año) == 1949 or int(año) == 1961 or int(año) == 1973 or int(año) == 1985 or int(año) == 1997 or int(año) == 2009 or int(año) == 2021 :
         zodiacal="Buey"
         image="http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Buey-300x257.jpg"
    elif int(año) == 1914 or int(año) == 1926 or int(año) == 1938 or int(año) == 1950 or int(año) == 1962 or int(año) == 1974 or int(año) == 1986 or int(año) == 1998 or int(año) == 2010 or int(año) == 2022 :
         zodiacal="Tigre"
         image="http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Tigre-300x257.jpg"
    elif int(año) == 1915 or int(año) == 1927 or int(año) == 1939 or int(año) == 1951 or int(año) == 1963 or int(año) == 1975 or int(año) == 1987 or int(año) == 1999 or int(año) == 2011 or int(año) == 2023 :
         zodiacal="Conejo"
         image="http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Conejo-300x257.jpg"
    elif int(año) == 1916 or int(año) == 1928 or int(año) == 1940 or int(año) == 1952 or int(año) == 1964 or int(año) == 1976 or int(año) == 1988 or int(año) == 2000 or int(año) == 2012 :
         zodiacal="Dragon"
         image="http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Dragon-300x257.jpg"
    elif int(año) == 1917 or int(año) == 1929 or int(año) == 1941 or int(año) == 1953 or int(año) == 1965 or int(año) == 1977 or int(año) == 1989 or int(año) == 2001 or int(año) == 2013 :
         zodiacal="Serpiente"
         image="http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Serpiente-300x257.jpg"
    elif int(año) == 1918 or int(año) == 1930 or int(año) == 1942 or int(año) == 1954 or int(año) == 1966 or int(año) == 1978 or int(año) == 1990 or int(año) == 2002 or int(año) == 2014 :
         zodiacal="Caballo"
         image="http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Caballo-300x257.jpg"
    elif int(año) == 1919 or int(año) == 1931 or int(año) == 1943 or int(año) == 1955 or int(año) == 1967 or int(año) == 1979 or int(año) == 1991 or int(año) == 2003 or int(año) == 2015 :
         zodiacal="Oveja"    
         image="http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Cabra-300x257.jpg"
    elif int(año) == 1920 or int(año) == 1932 or int(año) == 1944 or int(año) == 1956 or int(año) == 1968 or int(año) == 1980 or int(año) == 1992 or int(año) == 2004 or int(año) == 2016 :
         zodiacal="Mono"
         image="http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Mono-300x257.jpg"
    elif int(año) == 1921 or int(año) == 1933 or int(año) == 1945 or int(año) == 1957 or int(año) == 1969 or int(año) == 1981 or int(año) == 1993 or int(año) == 2005 or int(año) == 2017 :
         zodiacal="Gallo"
         image="http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Gallo-300x257.jpg"
    elif int(año) == 1922 or int(año) == 1934 or int(año) == 1946 or int(año) == 1958 or int(año) == 1970 or int(año) == 1982 or int(año) == 1994 or int(año) == 2006 or int(año) == 2018 :
         zodiacal="Perro"
         image="http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Perro-300x257.jpg"
    elif int(año) == 1923 or int(año) == 1935 or int(año) == 1947 or int(año) == 1959 or int(año) == 1971 or int(año) == 1983 or int(año) == 1995 or int(año) == 2007 or int(año) == 2019 :
         zodiacal="Cerdo"
         image="http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Cerdo-300x257.jpg"
    else :
        zodiacal ="No tiene mijo"
    cont=0
    if p1=="b":
        cont=1

    if p2=="b":
        cont=cont+1
    
    if p3=="b":
        cont=cont+1
    
    if p4=="b":
        cont=cont+1
    
    if p5=="b":
        cont=cont+1
    
   
    return render_template("examenPruebaRespuesta.html", edad=edad, zodiacal=zodiacal, nombre=nombre,apa=apa,ama=ama, cont=cont, image=image)


if __name__=="__main__":
    app.run(debug=True,port=3000)