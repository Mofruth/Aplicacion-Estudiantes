from Config.database_connection import create_connection

class Padre:
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
                    query = "SELECT * FROM padres WHERE correo = %s"
                    cursor.execute(query, (correo,))
                    padre_data = cursor.fetchone()
                    if padre_data:
                        return Padre(
                            id=padre_data['id'],
                            nombre=padre_data['nombre'],
                            correo=padre_data['correo'],
                            contraseña=padre_data['contraseña']
                        )
            except Exception as e:
                print(f"Error al obtener padre por correo: {e}")
            finally:
                conexion.close()
        return None