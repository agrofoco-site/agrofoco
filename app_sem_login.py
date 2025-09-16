# app_sem_login.py
# -*- coding: utf-8 -*-
import streamlit as st
from PIL import Image
from estilos import set_page_title   # ✅ sem subpasta

set_page_title("AgroFoco - Simuladores")

# ✅ logo direto na raiz
logo = Image.open("logo.png")
st.sidebar.image(logo, width=150)

menu = st.sidebar.radio(
    "Menu principal",
    ["Tela Institucional", "Simulador: Peso a Menor"],
    key="main_menu"
)

if menu == "Tela Institucional":
    import simuladores as modulo   # ✅ sem pasta "paginas"
elif menu == "Simulador: Peso a Menor":
    import simulador_peso_menor as modulo   # ✅ sem pasta "paginas"

modulo.app()

