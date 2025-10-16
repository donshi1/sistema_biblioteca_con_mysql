#!/usr/bin/env python3
"""
SISTEMA DE DIAGNÓSTICO - Para identificar problemas
"""

import mysql.connector
from mysql.connector import Error
import sys
import os

def test_conexion_bd():
    """Prueba la conexión a la base de datos"""
    print("\n" + "="*50)
    print("🔍 TEST DE CONEXIÓN A BASE DE DATOS")
    print("="*50)
    
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Cambia si tienes contraseña
            database="biblioteca"
        )
        
        if conexion.is_connected():
            print("✅ CONEXIÓN EXITOSA")
            
            # Verificar si la base de datos existe
            cursor = conexion.cursor()
            cursor.execute("SHOW DATABASES LIKE 'biblioteca'")
            resultado = cursor.fetchone()
            
            if resultado:
                print("✅ Base de datos 'biblioteca' encontrada")
                
                # Verificar tablas
                cursor.execute("USE biblioteca")
                cursor.execute("SHOW TABLES")
                tablas = cursor.fetchall()
                
                print("📊 Tablas encontradas:")
                for tabla in tablas:
                    print(f"   - {tabla[0]}")
                
                # Verificar datos en cada tabla
                for tabla in ['libros', 'usuarios', 'prestamos']:
                    cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                    count = cursor.fetchone()[0]
                    print(f"   📦 {tabla}: {count} registros")
                    
                    if count > 0:
                        cursor.execute(f"SELECT * FROM {tabla} LIMIT 3")
                        registros = cursor.fetchall()
                        print(f"     Primeros registros: {registros}")
            
            else:
                print("❌ Base de datos 'biblioteca' NO encontrada")
                print("💡 Ejecuta el archivo: database/01_biblioteca_schema.sql")
            
            cursor.close()
            conexion.close()
            
    except Error as e:
        print(f"❌ ERROR DE CONEXIÓN: {e}")
        print("💡 Soluciones posibles:")
        print("   1. Verifica que MySQL esté ejecutándose")
        print("   2. Verifica el usuario y contraseña")
        print("   3. Crea la base de datos con: database/01_biblioteca_schema.sql")

def test_imports():
    """Prueba que los imports funcionen correctamente"""
    print("\n" + "="*50)
    print("🔍 TEST DE IMPORTS")
    print("="*50)
    
    try:
        # Agregar src al path
        sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
        
        from database_connection import ConexionBD
        from library_models import Libro, Usuario, Prestamo
        
        print("✅ Todos los imports funcionan correctamente")
        
        # Probar la clase Libro
        libro = Libro()
        print("✅ Clase Libro instanciada correctamente")
        
        return True
        
    except ImportError as e:
        print(f"❌ ERROR EN IMPORTS: {e}")
        return False

def test_obtener_libros():
    """Prueba específicamente la función de obtener libros"""
    print("\n" + "="*50)
    print("🔍 TEST OBTENER LIBROS")
    print("="*50)
    
    try:
        sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
        from library_models import Libro
        
        print("📚 Obteniendo libros...")
        libros = Libro.obtener_todos()
        
        print(f"📊 Se encontraron {len(libros)} libros")
        
        if libros:
            for i, libro in enumerate(libros, 1):
                print(f"   {i}. {libro}")
        else:
            print("💡 No hay libros en la base de datos")
            print("💡 Ejecuta: database/02_datos_prueba.sql")
            
    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    print("🚀 INICIANDO DIAGNÓSTICO DEL SISTEMA")
    
    # Ejecutar tests
    test_conexion_bd()
    test_imports()
    test_obtener_libros()
    
    print("\n" + "="*50)
    print("🎯 DIAGNÓSTICO COMPLETADO")
    print("="*50)