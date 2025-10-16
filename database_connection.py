import mysql.connector
from mysql.connector import Error

class ConexionBD:
    def __init__(self):
        # ⚠️ ACTUALIZA CON TU CONTRASEÑA REAL:
        self.host = "localhost"
        self.user = "root"
        self.password = "toor"  # ⬅️ ⚠️ CAMBIA ESTO
        self.database = "biblioteca"
        self.port = 3306
        
        self.conexion = None
    
    def conectar(self):
        """Establece la conexión con la base de datos"""
        try:
            print("🔌 Conectando a MySQL...")
            
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,  # ← Ahora con contraseña real
                database=self.database,
                port=self.port
            )
            
            if self.conexion.is_connected():
                print("✅ Conexión exitosa a MySQL")
                return True
                
        except Error as e:
            print(f"❌ Error de conexión: {e}")
            return False
    
    # El resto del código se mantiene igual...
    def desconectar(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("🔌 Conexión cerrada")
    
    def ejecutar_consulta(self, consulta, parametros=None):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(consulta, parametros or ())
            self.conexion.commit()
            return cursor.rowcount
        except Error as e:
            print(f"❌ Error en consulta: {e}")
            return 0
    
    def ejecutar_consulta_con_retorno(self, consulta, parametros=None):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            cursor.execute(consulta, parametros or ())
            return cursor.fetchall()
        except Error as e:
            print(f"❌ Error en consulta SELECT: {e}")
            return []