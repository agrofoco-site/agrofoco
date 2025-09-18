# app_sem_login.py
# -*- coding: utf-8 -*-
import streamlit as st
from PIL import Image
from estilos import set_page_title   # ✅ sem subpasta


# ─── Título da página ──────────────────────────────────────────────
set_page_title("AgroFoco - Simuladores")

# ─── Logo direto da raiz ───────────────────────────────────────────
logo = Image.open("logo.png")
st.sidebar.image(logo, width=150)

# ─── Menu lateral ──────────────────────────────────────────────────
menu = st.sidebar.radio(
    "MENU",[
        "AgroFoco",
        "Cáculo - Peso a Menor"],
    key="main_menu"
)

# ─── Importa o módulo correto conforme a escolha ──────────────────
if menu == "AgroFoco":
    import home as modulo  # ✅ nome novo aplicado aqui
elif menu == "Cáculo - Peso a Menor":
    import simulador_peso_menor as modulo  # ✅ nome correto com underline

# ─── Executa o app da página selecionada ──────────────────────────
modulo.app()
