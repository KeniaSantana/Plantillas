from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    arr=["Daniel","Miguel","Sagarnaga","Romo"]
    autor="Kenia Alejandra Santana Ruiz"
    return render_template("index.html", nombre= autor, amigos=arr)

@app.route("/")
def numeros():
    numeros=["1","10","100","1000","1000"]
    auto="Kenia Alejandra Santana Ruiz"
    return render_template("plan.html",nombre=auto, numE=numeros)

@app.route("/")
def colores():
    colores=["Azul","Rosa","Verde","Morado","Rojo","Amarillo"]
    r="Kenia Alejandra Santana Ruiz"
    return render_template("diferente.html",nombre=r, color=colores)

if __name__=="__main__":
    app.run(debug=True)