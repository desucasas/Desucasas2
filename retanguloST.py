import streamlit as st #Framework
import math as mt #Biblioteca
#Problema Retângulo
st.title("Problema Retângulo")
#Entrada de dados
base = st.number_input("Digite a base do retângulo:")
altura = st.number_input("Digite a altura do retângulo:")
#Processamento de dados
area = base * altura
perimetro = 2 * base + altura * 2
# diagonal = (base**2 + altura**2)**0.5
x = mt.pow(base,2) + mt.pow(altura,2)
diagonal = mt.sqrt(x)
#Saída de dados
st.write(f"A área do retângulo é {area}")
st.write(f"O perímetro do retângulo é {perimetro}")
st.write(f"A diagonal do retângulo é {diagonal}")
