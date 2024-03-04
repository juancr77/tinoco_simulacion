import random
import mysql.connector

# Conectarse a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="simulacion_prueba"
)
cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute("CREATE TABLE IF NOT EXISTS resultados_dado (id INT AUTO_INCREMENT PRIMARY KEY, resultado INT)")

# Función para lanzar el dado
def lanzar_dado():
    return random.randint(1, 6)

# Función para simular la tirada del dado y registrar el resultado en la base de datos
def simular_tiradas(n_tiradas):
    for _ in range(n_tiradas):
        resultado = lanzar_dado()
        cursor.execute("INSERT INTO resultados_dado (resultado) VALUES (%s)", (resultado,))
        conexion.commit()

# Ejecutar la simulación con 10 tiradas
simular_tiradas(10)

# Mostrar los resultados almacenados en la base de datos
cursor.execute("SELECT * FROM resultados_dado")
resultados = cursor.fetchall()
print("Resultados de las tiradas del dado:")
for resultado in resultados:
    print(resultado)

# Cerrar la conexión con la base de datos
conexion.close()
