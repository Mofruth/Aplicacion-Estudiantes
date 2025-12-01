from pymysql import Error
from Config.database_connection import create_connection
from Models.admin import Admin
from Models.profesor import Profesor
from Models.estudiante import Estudiante
from Models.padre import Padre
from werkzeug.security import check_password_hash

class Usuario:
    def __init__(self, id=None, nombre=None, correo=None, contraseña=None, tipo=None):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.tipo = tipo

    @classmethod
    def obtener_por_correo(cls, correo):
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor(dictionary=True)
                query = """
                SELECT 'admin' as tipo, id, nombre, correo, contraseña FROM administradores WHERE correo = %s
                UNION SELECT 'profesor' as tipo, id, nombre, correo, contraseña FROM profesores WHERE correo = %s
                UNION SELECT 'estudiante' as tipo, id, nombre, correo, contraseña FROM estudiantes WHERE correo = %s
                UNION SELECT 'padre' as tipo, id, nombre, correo, contraseña FROM padres WHERE correo = %s
                """
                cursor.execute(query, (correo, correo, correo, correo))
                usuario = cursor.fetchone()
                if usuario:
                    return cls(
                        id=usuario['id'],
                        nombre=usuario['nombre'],
                        correo=usuario['correo'],
                        contraseña=usuario['contraseña'],
                        tipo=usuario['tipo']
                    )
                return None
            except Error as e:
                print(f"Error al obtener usuario: {e}")
                return None
            finally:
                if conexion.is_connected():
                    cursor.close()
                    conexion.close()

    @staticmethod
    def autenticar(correo, contraseña):
        # Primero busca en administradores
        admin = Admin.obtener_por_correo(correo)
        if admin and check_password_hash(admin.contraseña, contraseña):
            admin.rol = 'admin'
            return admin
        # Luego busca en usuarios generales
        usuario = Usuario.obtener_por_correo(correo)
        if usuario and check_password_hash(usuario.contraseña, contraseña):
            usuario.rol = usuario.tipo  # tipo: 'profesor', 'estudiante', 'padre'
            return usuario
        return None