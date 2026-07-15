import streamlit as st
import sqlite3
import pandas as pd

st.title("Monitarização de Sensores Industriais")

# Ligar DB
conn = sqlite3.connect("sensores.db")
df = pd.read_sql_query("SELECT * FROM leituras", conn)

# Mostrar dados
st.dataframe(df.tail(10))

# Gráfico Interativo
st.line_chart(df.pivot_table(index="timestamp", columns="sensor", values="valor"))

