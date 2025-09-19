# home.py
# Tela inicial pública da AgroFoco

import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def app():
    # Define fundo visual com imagem fundo.png
    background_image = get_base64_of_bin_file("fundo.png")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                        url("data:image/png;base64,{background_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: white;
        }}

        h1, h2, h3, h4 {{
            color: white;
        }}

        h2 {{
            font-size: 34px !important;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }}

        .material-icons {{
            vertical-align: middle;
            font-size: 34px;
            margin-right: 0.4rem;
        }}

        .block-container {{
            padding-top: 4rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Título inicial
    st.markdown("<h1>Bem-vindo à AgroFoco</h1>", unsafe_allow_html=True)

    # SOBRE NÓS com ícone
    # Missão
    st.markdown("<h2>🏢 Sobre Nós</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-weight: 350; font-size: 34px;'>A AgroFoco oferece soluções gerenciais personalizadas para associações e produtores integrados, com foco em eficiência, sustentabilidade e fortalecimento da cadeia produtiva.</h3>", unsafe_allow_html=True)
  

    # Missão
    st.markdown("<h2>🎯 Missão</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-weight: 350; font-size: 34px;'>Levar inteligência para o campo com compromisso com o resultado.</h3>", unsafe_allow_html=True)

    # Visão
    st.markdown("<h2>👀 Visão</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-weight: 350; font-size: 34px;'>Ser referência nacional em tecnologia aplicada ao agronegócio.</h3>", unsafe_allow_html=True)

    # Valores
    st.markdown("<h2>🧭 Valores</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-weight: 350; font-size: 34px;'>Inovação, Comprometimento, Sustentabilidade, Ética e Resultado.</h3>", unsafe_allow_html=True)
