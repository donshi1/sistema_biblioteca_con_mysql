#!/usr/bin/env python3
"""
PRUEBA DE CONEXIÓN COMPATIBLE CON MYSQL WORKBENCH
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def test_workbench_compatibility():
    print("🔍 PRUEBA DE CONEXIÓN MYSQL WORKBENCH")
    print("=" * 50)
    
    try:
        from database_connection import ConexionBD
        
        print("🧪 Probando configuración de Workbench...")
        
        # Probar conexión
        db = ConexionBD()
        
        if db.conectar():
            print("🎉 ¡CONEXIÓN EXITOSA!")
            print("✅ Python puede conectarse a la misma base de datos que Workbench")
            
            # Verificar datos
            try:
                # Probar tablas
                tablas = db.ejecutar_consulta_con_retorno("SHOW TABLES")
                print(f"📊 Tablas encontradas: {len(tablas)}")
                
                # Probar libros
                libros = db.ejecutar_consulta_con_retorno("SELECT COUNT(*) as total FROM libros")
                print(f"📚 Libros en base de datos: {libros[0]['total']}")
                
                # Probar usuarios
                usuarios = db.ejecutar_consulta_con_retorno("SELECT COUNT(*) as total FROM usuarios")
                print(f"👥 Usuarios en base de datos: {usuarios[0]['total']}")
                
            except Exception as e:
                print(f"ℹ️  Info: {e}")
            
            db.desconectar()
            
            print("\n✅ ¡Todo listo! Ahora ejecuta: python run_system.py")
            
        else:
            print("\n🔧 AJUSTA LA CONFIGURACIÓN:")
            print("1. Abre MySQL Workbench")
            print("2. Mira los datos de tu conexión")
            print("3. Actualiza database_connection.py con ESOS mismos datos")
            
    except Exception as e:
        print(f"💥 ERROR: {e}")

if __name__ == "__main__":
    test_workbench_compatibility()