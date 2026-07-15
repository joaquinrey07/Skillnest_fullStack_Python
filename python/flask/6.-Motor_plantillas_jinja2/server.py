from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html",
    nombre="Mauryperkin",
    curso="Desarrollo Web con Flask",
    ciudad="Santiago",
    anio=2026,
    profesor=False)

@app.route("/exito")
def exito():
    return "¡Éxito!"
    

if __name__ == "__main__":
    app.run(debug=True)