import mysql.connector
from mysql.connector import Error

print("--- Iniciando prueba de conexión ---")

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Dejamos la contraseña vacía como acordamos
        database='biblioteca'
    )
    if connection.is_connected():
        print("\n¡ÉXITO! La conexión a la base de datos 'biblioteca' fue exitosa.")

except Error as e:
    print("\n¡FALLO! No se pudo conectar. Este es el error específico:")
    print(e)

finally:
    print("\n--- Prueba de conexión finalizada ---")