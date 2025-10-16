import socket

HOST = '127.0.0.1'
PORT = 3306

print("--- Iniciando prueba de red básica ---")
print(f"Intentando conectar a {HOST} en el puerto {PORT}...")

try:
    # Se crea un 'socket' de red
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)  # Se establece un tiempo de espera de 5 segundos
        s.connect((HOST, PORT))
        print("\n¡ÉXITO! La conexión de red al puerto 3306 fue exitosa.")
        print("Esto confirma que Python SÍ puede hacer conexiones y que MySQL está escuchando.")

except socket.timeout:
    print("\n¡FALLO! La conexión tardó demasiado (Timeout).")
    print("Causa probable: Un firewall o antivirus está bloqueando la conexión.")
except ConnectionRefusedError:
    print("\n¡FALLO! La conexión fue rechazada (ConnectionRefusedError).")
    print("Causa probable: El servidor de MySQL NO está en ejecución.")
except Exception as e:
    print(f"\n¡FALLO! Ocurrió un error de red inesperado: {e}")

print("\n--- Prueba de red finalizada ---")