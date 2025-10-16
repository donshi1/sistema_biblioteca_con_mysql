# 📚 Sistema de Biblioteca con MySQL y POO

## 🎯 Descripción del Proyecto
Sistema de gestión de biblioteca desarrollado en **Python** con **MySQL**, aplicando principios de **Programación Orientada a Objetos (POO)** y **encapsulamiento**. Permite administrar libros, usuarios y préstamos con persistencia en base de datos.

## 🚀 Características Principales
- **Gestión completa de libros** (CRUD)
- **Registro de usuarios** con tipos específicos
- **Control de préstamos** con validaciones
- **Interfaz por terminal** intuitiva
- **Encapsulamiento estricto** en todas las clases

## 🛠️ Tecnologías
- Python 3.13.9
- MySQL 8.0+
- mysql-connector-python
- Programación Orientada a Objetos

## 📁 Estructura del Proyecto
sistema-biblioteca-mysql/
├── database/ # Scripts SQL
├── src/ # Código fuente
├── docs/ # Documentación
├── run_system.py # Ejecutable
└── README.md # Este archivo

## 🗃️ Base de Datos
El sistema incluye:
- **5 usuarios** registrados
- **5 libros** en catálogo
- **5 préstamos** activos
- **Backup completo** en `database/03_backup_completo.sql`

## 🔒 Encapsulamiento Implementado
```python
class Libro:
    def __init__(self):
        self.__titulo = ""      # Atributo privado
        self.__autor = ""       # Atributo privado
    
    # Getters y Setters con validación
    def get_titulo(self): return self.__titulo
    def set_titulo(self, titulo): 
        if titulo.strip(): 
            self.__titulo = titulo.strip()
🖥️ Interfaz
https://docs/captura_menu.png
https://docs/captura_libros.png
# 1. Clonar repositorio
git clone https://github.com/donshi1/sistema-biblioteca-mysql.git

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar BD
mysql -u root -p < database/01_biblioteca_schema.sql
mysql -u root -p < database/02_datos_prueba.sql

# 4. Ejecutar sistema
python run_system.py
📋 Entregables Completados
✅ Código con repositorio en GitHub

✅ 5 usuarios, 5 libros, 5 préstamos

✅ Backup de base de datos

✅ Capturas de interfaz

✅ Explicación de encapsulamiento

Proyecto educativo - Sistema de Biblioteca con MySQL y POO
