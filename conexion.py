# conexion.py

import pymysql # <-- CAMBIO: Importamos la nueva librería
from pymysql import Error

class ConexionBD:
    """
    Gestiona la conexión con la base de datos MySQL usando PyMySQL.
    """
    def __init__(self, host='localhost', user='root', password='toor', database='biblioteca'):
        try:
            # CAMBIO: Usamos pymysql.connect() y el parámetro 'db'
            self.connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                db=database # <-- CAMBIO: PyMySQL usa 'db' en lugar de 'database'
            )
        except Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            self.connection = None

    def ejecutar_consulta(self, query, params=None):
        if self.connection is None:
            return []
        
        # El resto del código es muy similar porque ambas librerías
        # siguen un estándar de Python para bases de datos.
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, params or ())
                return cursor.fetchall()
            except Error as e:
                print(f"Error al ejecutar la consulta: {e}")
                return []

    def ejecutar_modificacion(self, query, params=None):
        if self.connection is None:
            return None
            
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, params or ())
                self.connection.commit()
                return cursor.lastrowid
            except Error as e:
                print(f"Error al ejecutar la modificación: {e}")
                self.connection.rollback()
                return None

    def cerrar_conexion(self):
        if self.connection:
            self.connection.close()
            print("Conexión a la base de datos cerrada.")