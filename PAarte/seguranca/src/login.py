# O seguinte código em Flask está vulnerável a SQL Injection. Corrija o problema aplicando boas práticas de segurançã

from flask import app, request, cursor

@app.route("/login")
def login():
    email = request.args.get("email")
    password = request.args.get("password")

#     query = f"SELECT * FROM users WHERE email = {email} AND password = {password}"

#     result = cursor.execute(query)

# ==================== SOLUÇÃO =================================

# A versão original concatena diretamente dados fornecidos pelo utilizador na string SQL -> Risco de SQL Injection
# A nova versão usará prepared statements com parâmetros (?) e tuplos -> Separando dados da lógica SQL
# Assim, mesmo que o utilizador insira código malicioso, este será tratado com texto original #

    query = "SELECT * FROM users WHERE email = ? AND password = ?"

    result = cursor.execute(query, (email, password))