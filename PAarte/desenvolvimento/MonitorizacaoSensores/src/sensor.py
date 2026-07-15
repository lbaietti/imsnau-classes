from fastapi import FastAPI
from pydantic import BaseModel
import random, sqlite3, datetime

app = FastAPI()

# Modelo dos dados recebidos
class SensorData(BaseModel):
    sensor: str
    valor: float
    timestamp: str

# Criar base de dados SQLite
conn = sqlite3.connect("sensores.db", check_same_thread=False)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS leituras (sensor TEXT, valor REAL, timestamp TEXT)""")
conn.commit()

@app.get("/simular")
def simular_dados():
    sensores = ["Temperatura", "Vibracao", "Pressao"]
    leitura = SensorData(
        sensor = random.choice(sensores),
        valor = round(random.uniform(20, 100), 2),
        timestamp = str(datetime.datetime.now())
        )

    # Guardar em BD
    cur.execute("INSERT INTO leituras VALUES (?, ?, ?)", (leitura.sesor, leitura.valor, leitura. timestamp))
    conn.commit()

    # Alerta simples
    alerta = None

    if leitura.sensor == "Temperatura" and leitura.valor > 80:
        alerta = "ALERTA ! Temperatura Elevada !"
    return {"dados": leitura.dict(), "alerta": alerta}

