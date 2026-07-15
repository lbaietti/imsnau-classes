from flask import Flask, request, jsonify, render_template
import json
import requests

app = Flask(__name__)
FICHEIRO = "participantes.json"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/registar", methods=["POST"])
def registar():
    dados = request.json
    response = requests.get(f"https://viacep.com.br/ws/{dados['codigo_postal']}/json/")
    localidade = response.json().get("localidade", "Desconhecida")
    participante = {
        "nome": dados["nome"],
        "email": dados["email"],
        "codigo_postal": dados["codigo_postal"],
        "localidade": localidade
    }
    try:
        with open(FICHEIRO, "r") as f:
            lista = json.load(f)
    except FileNotFoundError:
        lista = []
    lista.append(participante)
    with open(FICHEIRO, "w") as f:
        json.dump(lista, f, indent=2)
    return jsonify({"mensagem": "Registo efetuado com sucesso!"})
        