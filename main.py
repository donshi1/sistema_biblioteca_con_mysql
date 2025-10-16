# main.py

from conexion import ConexionBD
from modelos import Libro, Usuario
from datetime import date

# --- FUNCIONES DE LÓGICA ---

def registrar_libro(db):
    print("\n--- Registrar Nuevo Libro ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = int(input("Año de publicación: "))
    
    query = "INSERT INTO libros (titulo, autor, anio) VALUES (%s, %s, %s)"
    db.ejecutar_modificacion(query, (titulo, autor, anio))
    print("Libro registrado exitosamente.")

def listar_libros(db):
    print("\n--- Lista de Libros ---")
    query = "SELECT * FROM libros"
    resultados = db.ejecutar_consulta(query)
    
    if not resultados:
        print("No hay libros registrados.")
        return
        
    for res in resultados:
        libro = Libro(id=res[0], titulo=res[1], autor=res[2], anio=res[3], disponible=res[4])
        print(libro)

def registrar_usuario(db):
    print("\n--- Registrar Nuevo Usuario ---")
    nombre = input("Nombre: ")
    tipo = input("Tipo (ej. Estudiante, Profesor): ")
    
    query = "INSERT INTO usuarios (nombre, tipo) VALUES (%s, %s)"
    db.ejecutar_modificacion(query, (nombre, tipo))
    print("Usuario registrado exitosamente.")

def listar_usuarios(db):
    print("\n--- Lista de Usuarios ---")
    query = "SELECT * FROM usuarios"
    resultados = db.ejecutar_consulta(query)

    if not resultados:
        print("No hay usuarios registrados.")
        return

    for res in resultados:
        usuario = Usuario(id=res[0], nombre=res[1], tipo=res[2])
        print(usuario)

def registrar_prestamo(db):
    print("\n--- Registrar Nuevo Préstamo ---")
    id_libro = int(input("ID del libro a prestar: "))
    id_usuario = int(input("ID del usuario: "))

    query_libro = "SELECT disponible FROM libros WHERE id = %s"
    resultado_libro = db.ejecutar_consulta(query_libro, (id_libro,))
    
    if not resultado_libro or not resultado_libro[0][0]:
        print("Error: El libro no existe o no está disponible.")
        return

    fecha_prestamo = date.today()
    query_prestamo = "INSERT INTO prestamos (id_libro, id_usuario, fecha_prestamo) VALUES (%s, %s, %s)"
    db.ejecutar_modificacion(query_prestamo, (id_libro, id_usuario, fecha_prestamo))

    query_update = "UPDATE libros SET disponible = FALSE WHERE id = %s"
    db.ejecutar_modificacion(query_update, (id_libro,))
    
    print("Préstamo registrado exitosamente.")

# --- MENÚ PRINCIPAL ---

def mostrar_menu():
    print("\n--- 📚 Sistema de Gestión de Biblioteca ---")
    print("1. Registrar Libro")
    print("2. Listar Libros")
    print("3. Registrar Usuario")
    print("4. Listar Usuarios")
    print("5. Registrar Préstamo")
    print("0. Salir")

def main():
    # Usa password='' si no tienes contraseña
    db = ConexionBD(password='') 
    if db.connection is None:
        print("No se pudo conectar a la base de datos. El programa terminará.")
        return

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            registrar_libro(db)
        elif opcion == '2':
            listar_libros(db)
        elif opcion == '3':
            registrar_usuario(db)
        elif opcion == '4':
            listar_usuarios(db)
        elif opcion == '5':
            registrar_prestamo(db)
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
    
    db.cerrar_conexion()

# Punto de entrada del programa
# ESTAS SON LAS LÍNEAS QUE FALTABAN
if __name__ == "__main__":
    main()