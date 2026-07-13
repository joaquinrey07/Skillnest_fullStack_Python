from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "¡Bienvenido a nuestro servidor Flask!"

@app.route("/explorar")
def explorar():
    return "¿Qué ruta estás buscando? ¡Prueba con diferentes direcciones!"

@app.route("/perfil/<nombre>")
def perfil(nombre):
    print(nombre)
    return (f'Bienvenid@ {nombre}, a tu perfil personalizado en nuestra app')

@app.route("/repite/<int:veces>/<mensaje>")
def repite(veces, mensaje):
    return (mensaje + " ") * veces

@app.errorhandler(404)
def pagina_no_encontrada(error):
    # Devolvemos el mensaje personalizado y el código de estado 404
    return "¡Sobrecarga de rutas! No encontramos a dónde quieres ir, inténtalo de nuevo.", 404

if __name__ == "__main__":
    app.run(debug=True)