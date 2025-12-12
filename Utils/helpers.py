"""
Funciones auxiliares y utilidades para el proyecto Campus
"""

from datetime import datetime
from Config.database_connection import create_connection


def obtener_estadisticas_generales():
    """Obtiene estadísticas generales del sistema."""
    conexion = create_connection()
    stats = {
        'total_estudiantes': 0,
        'total_profesores': 0,
        'total_materias': 0,
        'total_padres': 0
    }
    
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) AS total FROM estudiantes")
            stats['total_estudiantes'] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) AS total FROM profesores")
            stats['total_profesores'] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) AS total FROM materias")
            stats['total_materias'] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) AS total FROM padres")
            stats['total_padres'] = cursor.fetchone()[0]
        except Exception as e:
            print(f"Error al obtener estadísticas generales: {e}")
        finally:
            cursor.close()
            conexion.close()
    
    return stats


def formatear_fecha(fecha):
    """Formatea una fecha al formato dd/mm/yyyy HH:MM."""
    if isinstance(fecha, str):
        return fecha
    try:
        return fecha.strftime("%d/%m/%Y %H:%M")
    except:
        return str(fecha)


def validar_correo(correo):
    """Valida si el correo tiene un formato válido."""
    import re
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, correo) is not None


def calcular_promedio(valores):
    """Calcula el promedio de una lista de valores numéricos."""
    if not valores or len(valores) == 0:
        return 0
    return sum(valores) / len(valores)


def obtener_dia_semana_numero(dia_nombre):
    """Convierte el nombre de un día a número (0=Lunes, 6=Domingo)."""
    dias = {
        'Lunes': 0, 'Martes': 1, 'Miércoles': 2, 'Jueves': 3,
        'Viernes': 4, 'Sábado': 5, 'Domingo': 6
    }
    return dias.get(dia_nombre, -1)


def obtener_nombre_dia(numero):
    """Convierte el número de día a nombre."""
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    return dias[numero] if 0 <= numero < len(dias) else 'Desconocido'


def verificar_tabla_existe(nombre_tabla):
    """Verifica si una tabla existe en la base de datos."""
    conexion = create_connection()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute(f"SHOW TABLES LIKE '{nombre_tabla}'")
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error al verificar tabla: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()
    return False
