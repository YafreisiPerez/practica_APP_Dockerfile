from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# Configuración de la base de datos desde variables de entorno
DB_HOST = os.getenv('DB_HOST', 'db')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_NAME = os.getenv('DB_NAME', 'testdb')

@app.route('/')
def hello_world():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if conn.is_connected():
            return "¡Hola, Mundo! Conectado a la base de datos MySQL."
    except mysql.connector.Error as e:
        return f"Error conectando a la base de datos: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
