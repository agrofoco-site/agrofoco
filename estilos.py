# estilos.py
import streamlit as st

def set_page_title(title: str):
    # Define título da aba e layout padrão
    st.set_page_config(
        page_title=title,
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # CSS global para estilização visual
    st.markdown("""
        <style>
            /* FUNDO GERAL DA PÁGINA */
            .stApp {
                background-color: #f4f6f8;           /* Cor do fundo geral */
                font-family: 'Segoe UI', sans-serif; /* Fonte global */
            }

            /* SIDEBAR */
            section[data-testid="stSidebar"] {
                background-color: #f0f2f6;           /* Fundo da sidebar */
                padding: 2rem 1rem;
            }

            /* TÍTULOS GERAIS */
            h1, h2, h3, h4, h5 {
                color: #004080;          /* Azul escuro */
                font-weight: bold;
            }

            /* TÍTULO EXPANDERS */
            .streamlit-expanderHeader {
                font-weight: bold;
                font-size: 16px;
                color: #1f5c8a;
            }

            /* BOTÕES PADRÃO DO STREAMLIT */
            .stButton > button {
                background-color: #1f5c8a;
                color: white;
                font-weight: bold;
                padding: 8px 20px;
                border-radius: 8px;
                border: none;
            }

            .stButton > button:hover {
                background-color: #154c6d;
            }

            /* INPUTS */
            input, .stNumberInput input {
                border-radius: 5px;
                padding: 0.4em;
                border: 1px solid #ccc;
            }

            /* SELECTBOX */
            div[data-baseweb="select"] {
                background-color: white;
                border: 1px solid #007BFF;
                border-radius: 10px;
                padding: 5px;
            }

            /* PLACEHOLDER DO SELECTBOX */
            .css-1wa3eu0-placeholder {
                color: #004080;
                font-weight: bold;
            }

            /* MÉTRICAS */
            .stMetric {
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 0.8em;
                margin: 0.2em 0.5em;
                background-color: #f9f9f9;
                color: #1f5c8a;
                font-weight: bold;
            }

            /* RADIO BUTTONS VISUAL MODERNO */
            div[role="radiogroup"] {
                gap: 0.6rem;
            }

            div[role="radiogroup"] label {
                color: #1a1a1a;
                font-weight: 600;
                font-size: 16px;
                padding: 0.3rem 0.5rem;
                border-radius: 5px;
                cursor: pointer;
            }

            div[role="radiogroup"] svg {
                color: #003366 !important; /* Azul escuro no ativo */
                width: 20px;
                height: 20px;
            }

            div[role="radiogroup"] svg path {
                stroke: #999;             /* Contorno do inativo */
                stroke-width: 1.5;
            }

            /* REMOVER SCROLL HORIZONTAL DESNECESSÁRIO */
            section.main > div {
                overflow-x: hidden;
            }
        </style>
    """, unsafe_allow_html=True)
