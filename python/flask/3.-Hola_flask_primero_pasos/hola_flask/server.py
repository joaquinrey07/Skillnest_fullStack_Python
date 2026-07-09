from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Modificacion al texto!"

@app.route("/nosotros")
def nosotros():
    return "¡Conocenos un poco mas!"

#Productos
@app.route("/productos")
def productos():
    return "¡En este momento no hay prodcutos disponibles!"
    
#Contacto
@app.route("/contacto")
def contacto():
    return "¡Conoce nuestors contactos contacto@preguntas.cl!"

if __name__ == "__main__":
    app.run(debug=True)