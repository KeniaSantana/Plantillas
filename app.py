from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    arr = ["Daniel", "Miguel", "Sagarnaga", "Romo"]
    autor = "Kenia Alejandra Santana Ruiz"
    return render_template("amigos.html", nombre=autor, amigos=arr)

@app.route("/numeros")
def numeros():
    numeros = ["1", "10", "100", "1000", "10000"]
    return render_template("num.html", numE=numeros)

@app.route("/colores")
def colores():
    colores = ["Azul", "Rosa", "Verde", "Morado", "Rojo", "Amarillo"]
    return render_template("color.html", colores=colores)

@app.route("/batman")
def batman():
    batman = ["Batman", "Nightwing", "Robin", "Red Hood", "Red Robin"]
    return render_template("bat.html", personajes=batman)

if __name__=="__main__":
    app.run(debug=True)