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
            font-size: 28px !important;
            font-weight: 800;
            margin-bottom: 0 rem;
        }}

        .material-icons {{
            vertical-align: middle;
            font-size: 30px;
            margin-right: 0.4rem;
        }}

        .block-container {{
            padding-top: 1rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Título inicial
    #st.markdown("<h1>Bem-vindo à AgroFoco</h1>", unsafe_allow_html=True)

    # SOBRE NÓS com ícone
    # Missão
    st.markdown("<h2>🏢 SOBRE NÓS</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-weight: 400; font-size: 34px;'>A AgroFoco oferece soluções gerenciais sob medida, promovendo eficiência, sustentabilidade e o fortalecimento da cadeia produtiva.</h3>", unsafe_allow_html=True)
  

    # Missão
    st.markdown("<h2>🎯 MISSÃO</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-weight: 400; font-size: 34px;'>Levar inteligência para o campo com compromisso com o resultado.</h3>", unsafe_allow_html=True)

    # Visão
    st.markdown("<h2>👀 VISÃO</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-weight: 400; font-size: 34px;'>Ser referência nacional em tecnologia aplicada ao agronegócio.</h3>", unsafe_allow_html=True)

    # Valores
    st.markdown("<h2>🧭 VALORES</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-weight: 400; font-size: 34px;'>Inovação, Comprometimento, Sustentabilidade, Ética e Resultado.</h3>", unsafe_allow_html=True)

   #  Experiência
    st.markdown("<h2>🧑‍💼 EXPERIÊNCIA</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-weight: 400; font-size: 34px;'>Mais de 15 anos levando tecnologia ao campo brasileiro.</h3>", unsafe_allow_html=True)

