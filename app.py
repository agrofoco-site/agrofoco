# app.py

import streamlit as st
import importlib
from PIL import Image
from estilos import set_page_title
import sqlite3
import bcrypt

# ===============================
# CONEXÃO COM SQLITE3
# ===============================
def get_connection():
    return sqlite3.connect("AGROFOCO.db")

# ===============================
# FUNÇÃO PARA VALIDAR LOGIN
# ===============================
def validar_usuario(usuario, senha):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT senha FROM usuarios WHERE usuario = ?", (usuario,))
    row = cur.fetchone()
    conn.close()

    if row:
        senha_hash = row[0].encode()   # senha armazenada (hash no banco)
        return bcrypt.checkpw(senha.encode(), senha_hash)
    return False


# ─── CONFIGURAÇÃO DA PÁGINA ─────────────────────────────────────
set_page_title("AgroFoco - Simuladores")

# ─── LOGO NA SIDEBAR ───────────────────────────────────────────
try:
    logo = Image.open("logo.png")
    st.sidebar.image(logo, use_container_width=True)
except FileNotFoundError:
    st.sidebar.warning("⚠️ Logo não encontrada (logo.png)")

# ─── INICIALIZA LOGIN NA SESSION ───────────────────────────────
if "logado" not in st.session_state:
    st.session_state.logado = False

if "usuario" not in st.session_state:
    st.session_state.usuario = ""

# ─── SE NÃO ESTIVER LOGADO: MOSTRA HOME + LOGIN ───────────────
if not st.session_state.logado:
    with st.sidebar:
        st.subheader("🔐 ACESSO RESTRITO")

        usuario = st.text_input("USUÁRIO")
        senha = st.text_input("SENHA", type="password")

        if st.button("ENTRAR"):
            if validar_usuario(usuario, senha):
                st.session_state.logado = True
                st.session_state.usuario = usuario
                st.rerun()
            else:
                st.error("❌ Usuário ou senha incorretos.")

    # Página pública
    import home
    home.app()
    st.stop()

# ─── SE ESTIVER LOGADO: MOSTRA MENU DE SIMULADORES ────────────
st.sidebar.success("✅ Você está logado!")
st.sidebar.write(f"Usuário: **{st.session_state.usuario}**")

st.sidebar.markdown("---")
opcao = st.sidebar.radio("📊 Simuladores Disponíveis", [
    "Cadastro Simples",  # ⬅️ Substituição aqui
    "Cálculo - Peso a Menor",
    "Cálculo - Alojamento a Menor",
    "Cálculo - Acerto de RIPI's",
    "Cálculo - Mortalidade",
    "Cálculo - Desempenho Geral",
    "🔓 Sair"
])

# ─── SAIR DO SISTEMA ───────────────────────────────────────────
if opcao == "🔓 Sair":
    st.session_state.logado = False
    st.session_state.usuario = ""
    st.rerun()
else:
    # ─── MAPEAMENTO DE MÓDULOS ───────────────────────────────
    modulos = {
        "Cadastro Simples": "cadastro_simples",  # ⬅️ Novo módulo 
        "Cálculo - Peso a Menor": "simulador_peso_menor",
        "Cálculo - Alojamento a Menor": "simulador_alojamento_menor",
        "Cálculo - Acerto de RIPI's": "simulador_ripi",
        "Cálculo - Mortalidade": "simulador_mortalidade",
        "Cálculo - Desempenho Geral": "simulador_desempenho",
    }

    # ─── IMPORTA E EXECUTA MÓDULO ─────────────────────────────
    modulo = importlib.import_module(modulos[opcao])
    modulo.app()
