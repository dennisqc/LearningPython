from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/saludo', methods=['GET'])
def saludo():
    return jsonify({"mensaje": "Hola desde mi API con Flask"})

@app.route('/sumar', methods=['POST'])
def sumar():
    datos = request.get_json()
    resultado = datos['a'] + datos['b']
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)
