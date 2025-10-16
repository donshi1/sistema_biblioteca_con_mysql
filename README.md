diferencias entre el codigo original y el actualizado: la mas evidente es su funcionalidad, en la original python no arrojaba nada respecto a la conexion, tenia clases estandares y era mas susceptible a errores.
en el actualizado se reorganizo todo, se crearon nuevos archivos (la excepcion fue en mysql), clases y otros archivos pruebas para comprobar la conexion entre python y mysql,
mensajes de éxito/error claros y específicos, indicadores visuales (emojis) para mejor experiencia, guías paso a paso para el usuario, validaciones en tiempo real con feedback inmediato.
DESCRIPCION: este es un proyecto biblioteca con python en visual studio code y mysql workbench, en el cual se aplican principios de POO y el encapsulamiento, este proyecto simula en funcionamiento basico de una biblioteca
en la cual se pemrite registrar libros, usuarios o prestamos dentro de la base de datos en mysql.
CARACTERISTICAS: gestion de libros (registrar, listar, buscar o eliminar.), registro de usuarios (diferentes tipos: estudiante, profesor, administrativo.), control de prestamos que lleva la disponibilidad de los libres
la interfaz es sencilla , tiene conexion persistente y validacion de datos en tiempo real.
principios de POO aplicados: encapsulamiento en todas las clases, abstraccion en metodos especializados y metodos estaticos.
se utilizo:Python 3.13.9, MySQL 8.0+, mysql-connector-python 8.1.0, Programación Orientada a Objetos y Git & GitHub para control de versiones.
estructura: 
sistema-biblioteca-mysql/
├── 📁 database/ # Scripts SQL y backup
│ ├── 01_biblioteca_schema.sql
│ ├── 02_datos_prueba.sql
│ └── 03_backup_completo.sql
├── 📁 src/ # Código fuente Python
│ ├── database_connection.py
│ ├── library_models.py
│ └── main_system.py
├── 📁 tests/ # Pruebas unitarias
│ └── test_library_system.py
├── 📁 docs/ # Documentación
│ ├── captura_menu.png
│ ├── captura_libros.png
│ ├── captura_usuarios.png
│ ├── captura_prestamos.png
│ └── diagrama_bd.txt
├── run_system.py # Ejecutable principal
├── requirements.txt # Dependencias
└── README.md 
📊 DIAGRAMA DE BASE DE DATOS - SISTEMA BIBLIOTECA
TABLAS:

📚 LIBROS
├── id (PK, INT, AUTO_INCREMENT)
├── titulo (VARCHAR(100), NOT NULL)
├── autor (VARCHAR(100), NOT NULL)
├── anio (INT)
└── disponible (BOOLEAN, DEFAULT TRUE)

👥 USUARIOS
├── id (PK, INT, AUTO_INCREMENT)
├── nombre (VARCHAR(100), NOT NULL)
└── tipo (VARCHAR(50), DEFAULT 'Estudiante')

🔄 PRÉSTAMOS
├── id (PK, INT, AUTO_INCREMENT)
├── id_usuario (FK → usuarios.id)
├── id_libro (FK → libros.id)
├── fecha_prestamo (DATE)
└── fecha_devolucion (DATE)

RELACIONES:

usuarios (1) ──────── (N) préstamos
libros (1) ────────── (N) préstamos
encapsulamiento implementado. 
