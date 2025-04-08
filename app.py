from flask import Flask, jsonify
import mysql.connector

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos MySQL
db_config = {
    "host": "localhost",
    "user": "usuarioBBDD",
    "password": "password",
    "database": "nameBBDD"
}

# Ruta principal que obtiene eventos desde la base de datos
@app.route('/', methods=['GET'])
def obtener_eventos():
    try:
        # Conectar a la base de datos
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor(dictionary=True)  # Resultados como diccionario

        # Ejecutar consulta
        cursor.execute("SELECT id_evento, nombre_evento, descripcion, lugar, creador, concat('', duracion) FROM Eventos")
        eventos = cursor.fetchall()

        # Cerrar conexión
        cursor.close()
        conexion.close()

        # Retornar eventos en formato JSON
        return jsonify(eventos)
    
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
