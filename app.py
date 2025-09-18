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
    "MENU", [
        "AgroFoco",
        "Cálculo - Aloj. a Menor",
        "Cálculo - Peso a Menor",
        "Cálculo - Acerto de RIPI's",
        "Cálculo - Mortalidade",
        "Cálculo - Viabilidade Econômica",
        "Cálculo - Desempenho Geral"
    ],
    key="main_menu"
)

# ─── Importa o módulo correto conforme a escolha ──────────────────
if menu == "AgroFoco":
    import home as modulo
elif menu == "Cálculo - Aloj. a Menor":
    import simulador_alojamento_menor as modulo
elif menu == "Cálculo - Peso a Menor":
    import simulador_peso_menor as modulo
elif menu == "Cálculo - Acerto de RIPI's":
    import simulador_ripi as modulo
elif menu == "Cálculo - Mortalidade":
    import simulador_mortalidade as modulo
elif menu == "Cálculo - Viabilidade Econômica":
    import simulador_viabilidade as modulo
elif menu == "Cálculo - Desempenho Geral":
    import simulador_desempenho as modulo

# ─── Executa o app da página selecionada ──────────────────────────
modulo.app()

