import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("piso.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x,y)

st.title("Prevendo o valor do piso")
st.divider()

diametro = st.number_input("digite o tamanho do diametro do piso:")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write (f" o valor do piso com diametro de {diametro:.2f}cm é de R${preco_previsto:.2f}.")
   