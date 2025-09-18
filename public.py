# public.py
# Página inicial pública (sem login)
import streamlit as st
import home  # carrega o home.py da raiz
from estilos import set_page_title

# Configuração da página pública
set_page_title("AgroFoco - Home Pública")

# Executa a Home
home.app()
