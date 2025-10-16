from library_models import Libro, Usuario, Prestamo
import datetime

class SistemaBiblioteca:
    """Clase principal del sistema de biblioteca"""
    
    def __init__(self):
        self.mostrar_banner()
    
    def mostrar_banner(self):
        """Muestra el banner del sistema"""
        print("=" * 60)
        print("        📚 SISTEMA DE BIBLIOTECA CON MYSQL 📚")
        print("=" * 60)
        print("            Programación Orientada a Objetos")
        print("                Encapsulamiento y BD MySQL")
        print("=" * 60)
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal"""
        print("\n🏠 MENÚ PRINCIPAL")
        print("1. 📖 Gestión de Libros")
        print("2. 👥 Gestión de Usuarios")
        print("3. 🔄 Gestión de Préstamos")
        print("4. 📊 Reportes y Consultas")
        print("5. ❌ Salir")
    
    def mostrar_menu_libros(self):
        """Muestra el menú de gestión de libros"""
        print("\n📖 GESTIÓN DE LIBROS")
        print("1. Registrar nuevo libro")
        print("2. Listar todos los libros")
        print("3. Buscar libro por ID")
        print("4. Eliminar libro")
        print("5. Volver al menú principal")
    
    def mostrar_menu_usuarios(self):
        """Muestra el menú de gestión de usuarios"""
        print("\n👥 GESTIÓN DE USUARIOS")
        print("1. Registrar nuevo usuario")
        print("2. Listar todos los usuarios")
        print("3. Buscar usuario por ID")
        print("4. Volver al menú principal")
    
    def mostrar_menu_prestamos(self):
        """Muestra el menú de gestión de préstamos"""
        print("\n🔄 GESTIÓN DE PRÉSTAMOS")
        print("1. Registrar nuevo préstamo")
        print("2. Listar préstamos activos")
        print("3. Devolver libro")
        print("4. Volver al menú principal")
    
    def gestionar_libros(self):
        """Maneja las operaciones con libros"""
        while True:
            self.mostrar_menu_libros()
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "1":
                self.registrar_libro()
            elif opcion == "2":
                self.listar_libros()
            elif opcion == "3":
                self.buscar_libro_por_id()
            elif opcion == "4":
                self.eliminar_libro()
            elif opcion == "5":
                break
            else:
                print("❌ Opción no válida. Intente nuevamente.")
    
    def gestionar_usuarios(self):
        """Maneja las operaciones con usuarios"""
        while True:
            self.mostrar_menu_usuarios()
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.listar_usuarios()
            elif opcion == "3":
                self.buscar_usuario_por_id()
            elif opcion == "4":
                break
            else:
                print("❌ Opción no válida. Intente nuevamente.")
    
    def gestionar_prestamos(self):
        """Maneja las operaciones con préstamos"""
        while True:
            self.mostrar_menu_prestamos()
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "1":
                self.registrar_prestamo()
            elif opcion == "2":
                self.listar_prestamos()
            elif opcion == "3":
                self.devolver_libro()
            elif opcion == "4":
                break
            else:
                print("❌ Opción no válida. Intente nuevamente.")
    
    def mostrar_reportes(self):
        """Muestra reportes del sistema"""
        print("\n📊 REPORTES DEL SISTEMA")
        
        try:
            # Libros disponibles
            libros = Libro.obtener_todos()
            libros_disponibles = [libro for libro in libros if libro.get_disponible()]
            libros_prestados = [libro for libro in libros if not libro.get_disponible()]
            
            print(f"\n📚 Libros en el sistema: {len(libros)}")
            print(f"✅ Libros disponibles: {len(libros_disponibles)}")
            print(f"📖 Libros prestados: {len(libros_prestados)}")
            
            # Usuarios
            usuarios = Usuario.obtener_todos()
            print(f"\n👥 Usuarios registrados: {len(usuarios)}")
            
            # Préstamos activos
            prestamos = Prestamo.obtener_todos()
            print(f"🔄 Préstamos activos: {len(prestamos)}")
            
            input("\nPresione Enter para continuar...")
            
        except Exception as e:
            print(f"❌ Error al generar reportes: {e}")
            input("Presione Enter para continuar...")
    
    def registrar_libro(self):
        """Registra un nuevo libro"""
        print("\n📝 REGISTRAR NUEVO LIBRO")
        
        try:
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            anio = int(input("Año de publicación: ").strip())
            
            libro = Libro()
            libro.set_titulo(titulo)
            libro.set_autor(autor)
            libro.set_anio(anio)
            
            if libro.guardar() > 0:
                print("✅ Libro registrado exitosamente!")
            else:
                print("❌ Error al registrar el libro")
                
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\nPresione Enter para continuar...")
    
    def listar_libros(self):
        """Lista todos los libros"""
        print("\n📚 LISTA DE LIBROS")
        
        try:
            libros = Libro.obtener_todos()
            
            if not libros:
                print("No hay libros registrados")
            else:
                for libro in libros:
                    print(libro)
                    
        except Exception as e:
            print(f"❌ Error al cargar libros: {e}")
        
        input("\nPresione Enter para continuar...")
    
    def buscar_libro_por_id(self):
        """Busca un libro por su ID"""
        try:
            libro_id = int(input("ID del libro a buscar: ").strip())
            libro = Libro.buscar_por_id(libro_id)
            
            if libro:
                print("\n🔍 LIBRO ENCONTRADO:")
                print(libro)
            else:
                print("❌ Libro no encontrado")
                
        except ValueError:
            print("❌ ID debe ser un número")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        input("\nPresione Enter para continuar...")
    
    def eliminar_libro(self):
        """Elimina un libro por su ID"""
        try:
            libro_id = int(input("ID del libro a eliminar: ").strip())
            libro = Libro.buscar_por_id(libro_id)
            
            if libro:
                print(f"Libro a eliminar: {libro}")
                confirmar = input("¿Está seguro? (s/n): ").strip().lower()
                
                if confirmar == 's':
                    if libro.eliminar() > 0:
                        print("✅ Libro eliminado exitosamente!")
                    else:
                        print("❌ Error al eliminar el libro")
            else:
                print("❌ Libro no encontrado")
                
        except ValueError:
            print("❌ ID debe ser un número")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        input("\nPresione Enter para continuar...")
    
    def registrar_usuario(self):
        """Registra un nuevo usuario"""
        print("\n👥 REGISTRAR NUEVO USUARIO")
        
        try:
            nombre = input("Nombre completo: ").strip()
            print("Tipos disponibles: Estudiante, Profesor, Administrativo")
            tipo = input("Tipo de usuario: ").strip()
            
            usuario = Usuario()
            usuario.set_nombre(nombre)
            usuario.set_tipo(tipo)
            
            if usuario.guardar() > 0:
                print("✅ Usuario registrado exitosamente!")
            else:
                print("❌ Error al registrar el usuario")
                
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\nPresione Enter para continuar...")
    
    def listar_usuarios(self):
        """Lista todos los usuarios"""
        print("\n👥 LISTA DE USUARIOS")
        
        try:
            usuarios = Usuario.obtener_todos()
            
            if not usuarios:
                print("No hay usuarios registrados")
            else:
                for usuario in usuarios:
                    print(usuario)
                    
        except Exception as e:
            print(f"❌ Error al cargar usuarios: {e}")
        
        input("\nPresione Enter para continuar...")
    
    def buscar_usuario_por_id(self):
        """Busca un usuario por su ID"""
        try:
            usuario_id = int(input("ID del usuario a buscar: ").strip())
            usuario = Usuario.buscar_por_id(usuario_id)
            
            if usuario:
                print("\n🔍 USUARIO ENCONTRADO:")
                print(usuario)
            else:
                print("❌ Usuario no encontrado")
                
        except ValueError:
            print("❌ ID debe ser un número")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        input("\nPresione Enter para continuar...")
    
    def registrar_prestamo(self):
        """Registra un nuevo préstamo"""
        print("\n🔄 REGISTRAR NUEVO PRÉSTAMO")
        
        try:
            # Mostrar usuarios disponibles
            usuarios = Usuario.obtener_todos()
            if not usuarios:
                print("❌ No hay usuarios registrados")
                input("Presione Enter para continuar...")
                return
            
            print("\n👥 USUARIOS DISPONIBLES:")
            for usuario in usuarios:
                print(usuario)
            
            id_usuario = int(input("\nID del usuario: ").strip())
            
            # Mostrar libros disponibles
            libros = Libro.obtener_todos()
            libros_disponibles = [libro for libro in libros if libro.get_disponible()]
            
            if not libros_disponibles:
                print("❌ No hay libros disponibles para préstamo")
                input("Presione Enter para continuar...")
                return
            
            print("\n📚 LIBROS DISPONIBLES:")
            for libro in libros_disponibles:
                print(libro)
            
            id_libro = int(input("\nID del libro: ").strip())
            fecha_prestamo = input("Fecha de préstamo (YYYY-MM-DD): ").strip()
            fecha_devolucion = input("Fecha de devolución (YYYY-MM-DD): ").strip()
            
            prestamo = Prestamo(id_usuario, id_libro, fecha_prestamo, fecha_devolucion)
            
            if prestamo.guardar() > 0:
                print("✅ Préstamo registrado exitosamente!")
            else:
                print("❌ Error al registrar el préstamo")
                
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\nPresione Enter para continuar...")
    
    def listar_prestamos(self):
        """Lista todos los préstamos activos"""
        print("\n🔄 PRÉSTAMOS ACTIVOS")
        
        try:
            prestamos = Prestamo.obtener_todos()
            
            if not prestamos:
                print("No hay préstamos activos")
            else:
                for prestamo in prestamos:
                    print(prestamo)
                    
        except Exception as e:
            print(f"❌ Error al cargar préstamos: {e}")
        
        input("\nPresione Enter para continuar...")
    
    def devolver_libro(self):
        """Registra la devolución de un libro"""
        try:
            prestamo_id = int(input("ID del préstamo a devolver: ").strip())
            
            # Buscar el préstamo
            prestamos = Prestamo.obtener_todos()
            prestamo_encontrado = None
            
            for prestamo in prestamos:
                if prestamo.get_id() == prestamo_id:
                    prestamo_encontrado = prestamo
                    break
            
            if prestamo_encontrado:
                print(f"Préstamo a devolver: {prestamo_encontrado}")
                confirmar = input("¿Confirmar devolución? (s/n): ").strip().lower()
                
                if confirmar == 's':
                    if prestamo_encontrado.devolver_libro() > 0:
                        print("✅ Libro devuelto exitosamente!")
                    else:
                        print("❌ Error al devolver el libro")
            else:
                print("❌ Préstamo no encontrado")
                
        except ValueError:
            print("❌ ID debe ser un número")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        input("\nPresione Enter para continuar...")
    
    def ejecutar(self):
        """Método principal que ejecuta el sistema"""
        try:
            while True:
                self.mostrar_menu_principal()
                opcion = input("\nSeleccione una opción: ").strip()
                
                if opcion == "1":
                    self.gestionar_libros()
                elif opcion == "2":
                    self.gestionar_usuarios()
                elif opcion == "3":
                    self.gestionar_prestamos()
                elif opcion == "4":
                    self.mostrar_reportes()
                elif opcion == "5":
                    print("\n👋 ¡Gracias por usar el Sistema de Biblioteca!")
                    break
                else:
                    print("❌ Opción no válida. Intente nuevamente.")
                    input("Presione Enter para continuar...")
                    
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrumpido por el usuario")
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            input("Presione Enter para continuar...")