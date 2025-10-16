#!/usr/bin/env python3
"""
SISTEMA DE BIBLIOTECA - ARCHIVO PRINCIPAL DE EJECUCIÓN
=====================================================
Este archivo inicia el Sistema de Biblioteca con MySQL y POO
"""

import sys
import os

# Agregar el directorio src al path para poder importar los módulos
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def main():
    """Función principal que inicia el sistema"""
    try:
        print("🚀 Iniciando Sistema de Biblioteca...")
        print("📚 Cargando módulos...")
        
        # Importar después de agregar el path
        from main_system import SistemaBiblioteca
        
        print("✅ Módulos cargados correctamente")
        print("🔌 Conectando con la base de datos...")
        
        # Crear e iniciar el sistema
        sistema = SistemaBiblioteca()
        print("✅ Sistema listo para usar")
        
        # Ejecutar el sistema
        sistema.ejecutar()
        
    except ImportError as e:
        print(f"❌ Error al importar módulos: {e}")
        print("💡 Asegúrate de que los archivos estén en la carpeta 'src/'")
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        print("💡 Verifica la configuración de la base de datos")
    
    finally:
        print("\n👋 Sesión terminada. ¡Hasta pronto!")

if __name__ == "__main__":
    main()