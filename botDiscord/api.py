
from flask import Flask, Response, jsonify
from flask_cors import CORS
from bot import asistentes
import time
from bot import member_to_dict
from bot import obtener_asistentes
app = Flask(__name__)
CORS(app)  # Permite solicitudes CORS desde cualquier dominio

# Ruta para obtener los asistentes en formato Server-Sent Events
@app.route('/asistentes')
def obtener_asistentes_api():
    def generar_eventos():
        with app.app_context():
            while True:
                # Convertir los objetos Member en diccionarios
                asistentes_dict = [member_to_dict(member) for member in asistentes] #esto tampoco se usa
                # Serializar los diccionarios en formato JSON
                json_data = jsonify(obtener_asistentes()) #esto no se usa porque cambie el code pero puede servir despues
                # Enviar los datos en formato Server-Sent Events
                yield 'data: {}\n\n'.format(obtener_asistentes())
                time.sleep(3)  # Pausa de 1 segundo antes de enviar la siguiente actualización

    return Response(generar_eventos(), mimetype='text/event-stream')

def run_api():
    app.run()





