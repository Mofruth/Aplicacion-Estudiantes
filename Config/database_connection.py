import mysql.connector
from mysql.connector import Error
from Config.config import Config


def create_connection():
    """Crea y devuelve una conexión a la base de datos usando Config."""
    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
