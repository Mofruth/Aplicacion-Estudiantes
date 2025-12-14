from flask import Blueprint, session, redirect, render_template
from Controllers.estudiante_controller import EstudianteController

estudiante_bp = Blueprint("estudiante", __name__)

@estudiante_bp.route("/estudiante/notas")
def mis_notas():
    usuario = session.get("usuario")
    if not usuario:
        return redirect("/login")

    notas = EstudianteController.obtener_notas(usuario["id"])
    return render_template("estudiante/mis_calificaciones.html", notas=notas)
