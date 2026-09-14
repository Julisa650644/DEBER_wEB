import os

import mysql.connector


def obtener_conexion():
    """Crea una conexión usando variables de entorno, sin exponer contraseñas."""
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        port=int(os.environ.get("DB_PORT", "3306")),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", ""),
        database=os.environ.get("DB_NAME", "ferreteria_casa_clavo"),
        charset="utf8mb4",
        collation="utf8mb4_unicode_ci",
    )
