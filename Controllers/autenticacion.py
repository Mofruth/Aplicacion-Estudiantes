from Models.usuario import Usuario

class AutenticacionController:

    @staticmethod
    def validar_login(correo, password):
        return Usuario.autenticar(correo, password)
