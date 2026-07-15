from flask import Flask, request, jsonify

app = Flask(__name__)
reservas = []

# Recebe pedido POST via API flask para efetuar uma reserva
@app.route("/reservar", methods=["POST"])

def reservar():
    data = request.get_json()
    reservas.append(data)
    return jsonify({"mensagem": "Reserva efetuada !"})

# Recebe pedido GET via API flask para ver a lista de reservas efetuadas
@app.route("\listar", methods=["GET"])

def listar():
    return jsonify(reservas)