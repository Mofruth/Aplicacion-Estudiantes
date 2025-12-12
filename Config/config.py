"""
Configuración centralizada del proyecto Campus
"""

import os
from datetime import timedelta

# Configuración de la aplicación Flask
class Config:
    """Configuración base."""
    SECRET_KEY = 'clave_secreta_gestion_estudiantil_2023'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
    # Configuración de base de datos
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = ''
    DB_NAME = 'GestionDeEstudiantes'
    
    # Email
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_PORT = 587
    EMAIL_HOST_USER = "kevin.esteban.cuero@correounivalle.edu.co"
    EMAIL_HOST_PASSWORD = "1234"
    
    # Rutas
    TEMPLATE_FOLDER = 'Views'
    STATIC_FOLDER = 'Static'
    
    # Configuraciones de sesión
    MAX_SESSION_TIME = 3600  # 1 hora en segundos


class DevelopmentConfig(Config):
    """Configuración para desarrollo."""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Configuración para producción."""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Configuración para testing."""
    DEBUG = True
    TESTING = True
    DB_NAME = 'GestionDeEstudiantes_test'


# Seleccionar configuración según el entorno
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def get_config(env='development'):
    """Obtiene la configuración según el entorno."""
    return config.get(env, config['default'])
