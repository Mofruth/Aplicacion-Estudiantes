from Config.database_connection import create_connection

class Admin:
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
                    query = "SELECT * FROM administradores WHERE correo = %s"
                    cursor.execute(query, (correo,))
                    admin_data = cursor.fetchone()
                    if admin_data:
                        return Admin(
                            id=admin_data['id'],
                            nombre=admin_data['nombre'],
                            correo=admin_data['correo'],
                            contraseña=admin_data['contraseña']
                        )
            except Exception as e:
                print(f"Error al obtener administrador por correo: {e}")
            finally:
                conexion.close()
        return None