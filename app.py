import streamlit as st
import importlib
from PIL import Image
import home  # carrega a tela pública
from estilos import set_page_title

# ===============================
# Função para carregar usuários e senhas de um arquivo txt
# ===============================
def carregar_usuarios(caminho="usuarios.txt"):
    usuarios = {}
    try:
        with open(caminho, "r") as f:
            for linha in f:
                linha = linha.strip()
                if ":" in linha:
                    user, pwd = linha.split(":", 1)
                    usuarios[user.strip()] = pwd.strip()
    except FileNotFoundError:
        st.error("⚠️ Arquivo de usuários não encontrado! Crie um 'usuarios.txt'")
    return usuarios


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
            usuarios = carregar_usuarios()

            if usuario in usuarios and usuarios[usuario] == senha:
                st.session_state.logado = True
                st.session_state.usuario = usuario   # guarda usuário logado
                st.success(f"✅ Bem-vindo, {usuario}!")
                st.rerun()
            else:
                st.error("❌ Usuário ou senha incorretos.")

    # Carrega a tela pública
    home.app()
    st.stop()

# ─── SE ESTIVER LOGADO: MOSTRA MENU DE SIMULADORES ────────────
st.sidebar.success("✅ Você está logado!")
st.sidebar.write(f"Usuário: **{st.session_state.usuario}**")

st.sidebar.markdown("---")
opcao = st.sidebar.radio("📊 Simuladores Disponíveis", [
    "Cálculo - Peso a Menor",    
    "Cálculo - Alojamento a Menor",
    "Cálculo - Acerto de RIPI's",
    "Cálculo - Mortalidade",
    "Cálculo - Viabilidade Econômica",
    "Cálculo - Desempenho Geral",
    "🔓 Sair"
])


# 🔒 FRASE DE ÁREA RESTRITA
#st.title("🔒 Área Restrita - AgroFoco")
st.info("Bem-vindo à área restrita. Selecione uma opção de simulador no menu lateral para continuar.")

# ─── SAIR DO SISTEMA ───────────────────────────────────────────
if opcao == "🔓 Sair":
    st.session_state.logado = False
    st.session_state.usuario = ""   # limpa usuário
    st.rerun()
else:
    # ─── MAPEAMENTO DE MÓDULOS (importação dinâmica) ───────────────
    modulos = {
        "Cálculo - Peso a Menor": "simulador_peso_menor",        
        "Cálculo - Alojamento a Menor": "simulador_alojamento_menor",
        "Cálculo - Acerto de RIPI's": "simulador_ripi",
        "Cálculo - Mortalidade": "simulador_mortalidade",
        "Cálculo - Viabilidade Econômica": "simulador_viabilidade",
        "Cálculo - Desempenho Geral": "simulador_desempenho",
    }

    # ─── IMPORTA E EXECUTA O MÓDULO ESCOLHIDO ──────────────────────
    modulo = importlib.import_module(modulos[opcao])
    modulo.app()



