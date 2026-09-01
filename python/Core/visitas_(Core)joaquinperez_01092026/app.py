import os

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for
)

app = Flask(__name__)

app.secret_key = os.getenv(
    "FLASK_SECRET_KEY",
    "clave-local-solo-desarrollo"
)


def regresar_inicio():
    """Vuelve a la página principal sin sumar una visita adicional."""
    session["ignorar_visita"] = True
    return redirect(url_for("inicio"))


@app.route("/")
def inicio():
    """Muestra el contador almacenado en la sesión."""

    if "visitas" not in session:
        session["visitas"] = 1

    elif not session.pop("ignorar_visita", False):
        session["visitas"] += 1

    if "reinicios" not in session:
        session["reinicios"] = 0

    return render_template(
        "index.html",
        visitas=session["visitas"],
        reinicios=session["reinicios"]
    )


@app.route("/aumentar-dos", methods=["POST"])
def aumentar_dos():
    """Incrementa el contador en dos unidades."""

    visitas_actuales = session.get("visitas", 0)
    session["visitas"] = visitas_actuales + 2

    return regresar_inicio()


@app.route("/aumentar", methods=["POST"])
def aumentar():
    """Incrementa el contador utilizando la cantidad ingresada."""

    entrada = request.form.get("cantidad", "").strip()

    try:
        cantidad = int(entrada)

        if cantidad <= 0:
            raise ValueError

    except ValueError:
        flash(
            "Ingresa un número entero mayor que cero.",
            "error"
        )
        return regresar_inicio()

    session["visitas"] = session.get("visitas", 0) + cantidad

    flash(
        f"Se agregaron {cantidad} visitas.",
        "success"
    )

    return regresar_inicio()


@app.route("/reiniciar", methods=["POST"])
def reiniciar():
    """Restablece el contador y aumenta el número de reinicios."""

    session["visitas"] = 0
    session["reinicios"] = session.get("reinicios", 0) + 1

    flash(
        "El contador de visitas fue reiniciado.",
        "success"
    )

    return regresar_inicio()


@app.route("/destruir_sesion")
def destruir_sesion():
    """Elimina todos los datos almacenados en la sesión."""

    session.clear()

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)
