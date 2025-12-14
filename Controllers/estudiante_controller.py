from Models.nota import Nota
from Models.horario import Horario

class EstudianteController:

    @staticmethod
    def obtener_notas(id_estudiante):
        return Nota.obtener_por_estudiante(id_estudiante)

    @staticmethod
    def obtener_horario(id_estudiante):
        return Horario.obtener_por_estudiante(id_estudiante)
