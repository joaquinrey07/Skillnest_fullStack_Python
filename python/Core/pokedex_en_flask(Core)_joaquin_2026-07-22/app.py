import unicodedata
from flask import Flask, render_template

app = Flask(__name__)


def limpiar_caracteres(texto: str) -> str:
    normalizado = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in normalizado if not unicodedata.combining(c)).lower()


# Filtro disponible en HTML como {{ valor | slug }}
app.jinja_env.filters["slug"] = limpiar_caracteres


# Base de datos ficticia de Pokémon
lista_pokemon = [
    {"id": 1, "nombre": "Bulbasaur", "tipo": "Planta/Veneno", "imagen": "bulbasaur.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"},
    {"id": 4, "nombre": "Charmander", "tipo": "Fuego", "imagen": "charmander.png", "poder": 39, "altura": "0.6m", "peso": "8.5kg"},
    {"id": 7, "nombre": "Squirtle", "tipo": "Agua", "imagen": "squirtle.png", "poder": 44, "altura": "0.5m", "peso": "9.0kg"},
    {"id": 25, "nombre": "Pikachu", "tipo": "Eléctrico", "imagen": "pikachu.png", "poder": 35, "altura": "0.4m", "peso": "6.0kg"},
    {"id": 39, "nombre": "Jigglypuff", "tipo": "Normal/Hada", "imagen": "jigglypuff.png", "poder": 115, "altura": "0.5m", "peso": "5.5kg"},
    {"id": 52, "nombre": "Meowth", "tipo": "Normal", "imagen": "meowth.png", "poder": 40, "altura": "0.4m", "peso": "4.2kg"},
    {"id": 54, "nombre": "Psyduck", "tipo": "Agua", "imagen": "psyduck.png", "poder": 50, "altura": "0.8m", "peso": "19.6kg"},
    {"id": 94, "nombre": "Gengar", "tipo": "Fantasma/Veneno", "imagen": "gengar.png", "poder": 60, "altura": "1.5m", "peso": "40.5kg"},
    {"id": 95, "nombre": "Onix", "tipo": "Roca/Tierra", "imagen": "onix.png", "poder": 35, "altura": "8.8m", "peso": "210.0kg"},
    {"id": 143, "nombre": "Snorlax", "tipo": "Normal", "imagen": "snorlax.png", "poder": 160, "altura": "2.1m", "peso": "460.0kg"}
]



# Mostrar todos los Pokémon
@app.route("/pokemon")
def ver_pokedex_completa():

    return render_template(
        "pokemon.html",
        pokemones=lista_pokemon,
        titulo="Todos los Pokémon"
    )



# Buscar Pokémon por nombre
@app.route("/pokemon/nombre/<string:nombre>")
def encontrar_por_nombre(nombre):

    pokemon = next(
        (p for p in lista_pokemon if p["nombre"].lower() == nombre.lower()),
        None
    )

    if pokemon is None:

        mensaje = f'No pudimos encontrar información sobre "{nombre}" en nuestra Pokédex.'

        return mostrar_error_pokemon(mensaje)


    return render_template(
        "pokemon.html",
        pokemones=[pokemon],
        titulo=f"Pokémon: {pokemon['nombre']}"
    )



# Buscar Pokémon por número
@app.route("/pokemon/id/<int:numero>")
def buscar_pokemon_id(numero):

    pokemon = next(
        (p for p in lista_pokemon if p["id"] == numero),
        None
    )


    if pokemon is None:

        mensaje = f'No pudimos encontrar información sobre el Pokémon #{numero} en nuestra Pokédex.'

        return mostrar_error_pokemon(mensaje)


    return render_template(
        "pokemon.html",
        pokemones=[pokemon],
        titulo=f"Pokémon: {pokemon['nombre']}"
    )



# Mostrar cantidad específica de Pokémon
@app.route("/pokemon/cantidad/<int:cantidad>")
def ver_primeros_pokemon(cantidad):

    seleccion = lista_pokemon[:cantidad]

    return render_template(
        "pokemon.html",
        pokemones=seleccion,
        titulo=f"Primeros {cantidad} Pokémon"
    )



# Página cuando no existe un Pokémon
def mostrar_error_pokemon(mensaje: str):

    return render_template(
        "404.html",
        mensaje=mensaje
    )



# Error 404 general
@app.errorhandler(404)
def error_pagina_inexistente(error):

    mensaje = "La página que buscas no existe en nuestra Pokédex."

    return render_template(
        "404.html",
        mensaje=mensaje
    ), 404



if __name__ == "__main__":

    app.run(debug=True)
