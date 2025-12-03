from Config.database_connection import create_connection

class Profesor:
    def __init__(self, id, nombre, correo, contraseña):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

    @staticmethod
    def obtener_por_correo(correo):
        conexion = create_connection()
        if conexion:
            try:
                with conexion.cursor(dictionary=True) as cursor:
                    query = "SELECT * FROM profesores WHERE correo = %s"
                    cursor.execute(query, (correo,))
                    prof_data = cursor.fetchone()
                    if prof_data:
                        return Profesor(
                            id=prof_data['id'],
                            nombre=prof_data['nombre'],
                            correo=prof_data['correo'],
                            contraseña=prof_data['contraseña']
                        )
            except Exception as e:
                print(f"Error al obtener profesor por correo: {e}")
            finally:
                conexion.close()
        return None