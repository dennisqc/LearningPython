from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos en memoria
tareas = [
    {"id": 1, "titulo": "Estudiar Python", "completado": False},
    {"id": 2, "titulo": "Consumir API", "completado": False}
]

@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    return jsonify(tareas)


@app.route('/tareas', methods=['POST'])
def crear_tarea():
    nueva_tarea = request.get_json()
    nueva_tarea['id'] = len(tareas) + 1
    nueva_tarea['completado'] = False
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

@app.route('/tareas/<int:id>', methods=['PUT'])
def completar_tarea(id):
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['completado'] = True
            return jsonify(tarea)
    return jsonify({"error": "Tarea no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
