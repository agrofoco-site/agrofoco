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

# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
set_page_title("AgroFoco - Simuladores")

# ===============================
# LOGO NA SIDEBAR
# ===============================
try:
    logo = Image.open("logo.png")
    st.sidebar.image(logo, use_container_width=True)
except FileNotFoundError:
    st.sidebar.warning("⚠️ Logo não encontrada (logo.png)")

# ===============================
# INICIALIZA SESSION STATE
# ===============================
if "logado" not in st.session_state:
    st.session_state.logado = False
if "usuario" not in st.session_state:
    st.session_state.usuario = ""

# ===============================
# ÁREA DE LOGIN
# ===============================
if not st.session_state.logado:
    with st.sidebar:
        st.subheader("🔐 ACESSO RESTRITO")

        usuario = st.text_input("USUÁRIO", key="login_usuario")
        senha = st.text_input("SENHA", type="password", key="login_senha")

        if st.button("ENTRAR", key="btn_login"):
            if validar_usuario(usuario, senha):
                st.session_state.logado = True
                st.session_state.usuario = usuario
                st.success("✅ Login realizado com sucesso!")
            else:
                st.error("❌ Usuário ou senha incorretos.")

    # Página pública
    import home
    home.app()
    st.stop()

# ===============================
# ÁREA LOGADA
# ===============================
st.sidebar.success("✅ Você está logado!")
st.sidebar.write(f"Usuário: **{st.session_state.usuario}**")

st.sidebar.markdown("---")

opcao = st.sidebar.radio(
    "📊 Simuladores Disponíveis",
    [
        "Cadastro Simples",
        "Cálculo - Peso a Menor",
        "Cálculo - Alojamento a Menor",
        "Cálculo - Acerto de RIPI's",
        "Cálculo - Mortalidade",
        "Cálculo - Desempenho Geral",
        "🔓 Sair"
    ],
    key="menu_simuladores"
)

# ===============================
# SAIR DO SISTEMA
# ===============================
if opcao == "🔓 Sair":
    st.session_state.logado = False
    st.session_state.usuario = ""
    st.experimental_rerun()
else:
    # ===============================
    # MAPEAMENTO DE MÓDULOS
    # ===============================
    modulos = {
        "Cadastro Simples": "cadastro_simples",
        "Cálculo - Peso a Menor": "simulador_peso_menor",
        "Cálculo - Alojamento a Menor": "simulador_alojamento_menor",
        "Cálculo - Acerto de RIPI's": "simulador_ripi",
        "Cálculo - Mortalidade": "simulador_mortalidade",
        "Cálculo - Desempenho Geral": "simulador_desempenho",
    }

    # ===============================
    # IMPORTA E EXECUTA MÓDULO
    # ===============================
    modulo = importlib.import_module(modulos[opcao])
    modulo.app()
