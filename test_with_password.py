#!/usr/bin/env python3
"""
PRUEBA CON CONTRASEÑA - Versión segura
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def test_with_password():
    print("🔐 PRUEBA CON CONTRASEÑA")
    print("=" * 50)
    
    try:
        from database_connection import ConexionBD
        
        print("🔌 Probando conexión con contraseña...")
        
        db = ConexionBD()
        
        if db.conectar():
            print("🎉 ¡CONEXIÓN EXITOSA CON CONTRASEÑA!")
            
            # Verificar datos
            tablas = db.ejecutar_consulta_con_retorno("SHOW TABLES")
            print(f"📊 Tablas en biblioteca: {len(tablas)}")
            
            for tabla in tablas:
                print(f"   - {tabla['Tables_in_biblioteca']}")
            
            db.desconectar()
            print("\n✅ ¡Todo funciona! Ejecuta: python run_system.py")
        else:
            print("\n❌ Aún hay problemas con la contraseña")
            print("💡 Verifica que la contraseña en database_connection.py")
            print("   sea EXACTAMENTE la misma que usas en MySQL Workbench")
            
    except Exception as e:
        print(f"💥 ERROR: {e}")

if __name__ == "__main__":
    test_with_password()