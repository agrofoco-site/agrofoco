# app.py
# -*- coding: utf-8 -*-
import streamlit as st
import importlib
from PIL import Image
import home  # carrega a tela pública
from estilos import set_page_title

# ─── CONFIGURAÇÃO DA PÁGINA ─────────────────────────────────────
set_page_title("AgroFoco - Simuladores")

# ─── LOGO NA SIDEBAR ───────────────────────────────────────────
logo = Image.open("logo.png")
st.sidebar.image(logo, use_container_width=True)

# ─── INICIALIZA LOGIN NA SESSION ───────────────────────────────
if "logado" not in st.session_state:
    st.session_state.logado = False

# ─── SE NÃO ESTIVER LOGADO: MOSTRA HOME + LOGIN ───────────────
if not st.session_state.logado:
    with st.sidebar:
        st.subheader("🔐 ACESSO RESTRITO")
        usuario = st.text_input("USUÁRIO")
        senha = st.text_input("SENHA", type="password")
        if st.button("ENTRAR"):
            # ⚠️ LOGIN SIMPLES - SUBSTITUA POR LÓGICA REAL DEPOIS
            if usuario == "admin" and senha == "6881":
                st.session_state.logado = True
                st.success("✅ Login realizado com sucesso!")
                st.rerun()
            else:
                st.error("❌ Usuário ou senha incorretos.")

    # Carrega a tela pública
    home.app()
    st.stop()

# ─── SE ESTIVER LOGADO: MOSTRA MENU DE SIMULADORES ────────────
st.sidebar.markdown("---")
opcao = st.sidebar.radio("📊 Simuladores Disponíveis", [
    "Cálculo - Alojamento a Menor",
    "Cálculo - Peso a Menor",
    "Cálculo - Acerto de RIPI's",
    "Cálculo - Mortalidade",
    "Cálculo - Viabilidade Econômica",
    "Cálculo - Desempenho Geral",
    "🔓 Sair"
])

# ─── SAIR DO SISTEMA ───────────────────────────────────────────
if opcao == "🔓 Sair":
    st.session_state.logado = False
    st.rerun()

# ─── MAPEAMENTO DE MÓDULOS (importação dinâmica) ───────────────
modulos = {
    "Cálculo - Alojamento a Menor": "simulador_alojamento_menor",
    "Cálculo - Peso a Menor": "simulador_peso_menor",
    "Cálculo - Acerto de RIPI's": "simulador_ripi",
    "Cálculo - Mortalidade": "simulador_mortalidade",
    "Cálculo - Viabilidade Econômica": "simulador_viabilidade",
    "Cálculo - Desempenho Geral": "simulador_desempenho",
}

# ─── IMPORTA E EXECUTA O MÓDULO ESCOLHIDO ──────────────────────
modulo = importlib.import_module(modulos[opcao])
modulo.app()

