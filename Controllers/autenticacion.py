"""
    Controlador de autenticación para la aplicación.
    Provee métodos estáticos para validar credenciales y devolver instancias
    de usuario apropiadas según el tipo o el administrador autenticado.
    Métodos:
    - login(correo, contraseña):
        Valida el inicio de sesión de usuarios no administrativos.
        - Parámetros:
            - correo (str): correo electrónico del usuario.
            - contraseña (str): contraseña en texto plano a verificar contra el hash almacenado.
        - Comportamiento:
            - Busca un objeto Usuario mediante Usuario.obtener_por_correo(correo).
            - Verifica la contraseña usando check_password_hash(contrasena_almacenada, contraseña).
            - Si la verificación es correcta, devuelve una instancia correspondiente
              a la subclase del usuario (Profesor, Estudiante o Padre) construida
              con los datos del usuario.
        - Retorno:
            - Instancia de Profesor/Estudiante/Padre si la autenticación es exitosa.
            - None si no existe el usuario, la contraseña es incorrecta o el tipo
              de usuario no coincide con los esperados.
        - Notas:
            - No crea sesiones ni tokens; solo devuelve un objeto representativo.
            - Puede propagar excepciones si Usuario.obtener_por_correo u otras
              dependencias fallan.
    - login_por_correo(correo, contraseña):
        Valida el inicio de sesión de administradores por correo y contraseña.
        - Parámetros:
            - correo (str): correo electrónico del administrador.
            - contraseña (str): contraseña en texto plano a verificar contra el hash almacenado.
        - Comportamiento:
            - Intenta obtener un administrador mediante Admin.obtener_por_correo(correo).
            - Verifica la contraseña usando check_password_hash(contraseña_almacenada, contraseña).
            - Incluye impresiones de depuración para indicar si se encontró el administrador
              y si la contraseña es válida o no.
            - Atrapa excepciones internas y las registra (impresión), devolviendo None en caso de error.
        - Retorno:
            - Objeto administrador si la autenticación es exitosa.
            - None si no se encuentra el administrador, la contraseña es incorrecta o ocurre un error.
        - Notas:
            - Igual que login, no gestiona sesiones ni tokens; se limita a validar credenciales.
            - Contiene logs/prints de depuración que deberían retirarse o reemplazarse
              por un sistema de logging en producción.
    """
from Models.admin import Admin
from Models.profesor import Profesor
from Models.estudiante import Estudiante
from Models.padre import Padre
from werkzeug.security import check_password_hash

class AutenticacionController:
    
    @staticmethod
    def login(correo, contraseña):
        """Valida el inicio de sesión basado en correo y contraseña."""
        # Verifica si el correo pertenece a un usuario (no administradores)
        usuario = Usuario.obtener_por_correo(correo)
        if usuario and check_password_hash(usuario.contraseña, contraseña):
            if usuario.tipo == 'profesor':
                return Profesor(usuario.id, usuario.nombre, usuario.correo, usuario.contraseña)
            elif usuario.tipo == 'estudiante':
                return Estudiante(usuario.id, usuario.nombre, usuario.correo, usuario.contraseña)
            elif usuario.tipo == 'padre':
                return Padre(usuario.id, usuario.nombre, usuario.correo, usuario.contraseña)
        return None

    @staticmethod
    def login_por_correo(correo, contraseña):
        """Valida el inicio de sesión de un administrador por correo y contraseña."""
        try:
            administrador = Admin.obtener_por_correo(correo)
            if administrador:
                print(f"Administrador encontrado: {administrador.nombre}")  # Depuración
                if check_password_hash(administrador.contraseña, contraseña):
                    print("Contraseña válida")  # Depuración
                    return administrador
                else:
                    print("Contraseña inválida")  # Depuración
            else:
                print(f"No se encontró un administrador con el correo: {correo}")  # Depuración
        except Exception as e:
            print(f"Error en login_por_correo: {str(e)}")  # Depuración
        return None

def autenticar_usuario(correo, contraseña):
    # Buscar en administradores
    admin = Admin.obtener_por_correo(correo)
    if admin and check_password_hash(admin.contraseña, contraseña):
        return {'id': admin.id, 'nombre': admin.nombre, 'correo': admin.correo, 'tipo': 'admin'}

    # Buscar en profesores
    profesor = Profesor.obtener_por_correo(correo)
    if profesor and check_password_hash(profesor.contraseña, contraseña):
        return {'id': profesor.id, 'nombre': profesor.nombre, 'correo': profesor.correo, 'tipo': 'profesor'}

    # Buscar en estudiantes
    estudiante = Estudiante.obtener_por_correo(correo)
    if estudiante and check_password_hash(estudiante.contraseña, contraseña):
        return {'id': estudiante.id, 'nombre': estudiante.nombre, 'correo': estudiante.correo, 'tipo': 'estudiante'}

    # Buscar en padres
    padre = Padre.obtener_por_correo(correo)
    if padre and check_password_hash(padre.contraseña, contraseña):
        return {'id': padre.id, 'nombre': padre.nombre, 'correo': padre.correo, 'tipo': 'padre'}

    return None