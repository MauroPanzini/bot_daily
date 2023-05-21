
from flask import Flask, Response, jsonify
from flask_cors import CORS
from bot import asistentes
import time
from bot import member_to_dict
from bot import obtener_asistentes
import json

app = Flask(__name__)
CORS(app)  # Permite solicitudes CORS desde cualquier dominio

# Ruta para obtener los asistentes en formato Server-Sent Events
@app.route('/asistentes')
def obtener_asistentes_api():
    def generar_eventos():
        while True:
            data = obtener_asistentes()  # Obtener los datos en el formato deseado
            json_data = json.dumps(data)  # Convertir los datos a formato JSON
            yield 'data: {}\n\n'.format(json_data)
            time.sleep(1)

    return Response(generar_eventos(), mimetype='text/event-stream', headers={'Content-Type': 'application/json'})

def run_api():
    app.run()




