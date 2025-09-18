# home.py
import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def app():
    # ✅ fundo direto na raiz
    background_image = get_base64_of_bin_file("fundo.png")

    # CSS para aplicar como fundo de tela
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0.0), rgba(0,0,0,0)),
                        url("data:image/png;base64,{background_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: #4CA5BB;
        }}

        h1, h2, h3, h4, h5, h6 {{
            color: white;
        }}

        .block-container {{
            padding-top: 3rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Conteúdo da página
    st.markdown("## Sobre Nós")
    st.write("A AgroFoco oferece soluções gerenciais personalizadas para associações e produtores integrados, com foco em eficiência, sustentabilidade e fortalecimento da cadeia produtiva.")

    st.markdown("## Missão")
    st.write("Levar inteligência para o campo com compromisso com o resultado.")

    st.markdown("## Visão")
    st.write("Ser referência nacional em tecnologia aplicada ao agronegócio.")

    st.markdown("## Valores")
    st.write("Inovação, Comprometimento, Sustentabilidade, Ética, Resultado.")

    st.markdown("## Experiência")
    st.write("Mais de 15 anos levando tecnologia ao campo brasileiro.")
