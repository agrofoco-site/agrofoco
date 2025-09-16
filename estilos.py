# estilos.py
import streamlit as st

def set_page_title(title: str):
    st.set_page_config(
        page_title=title,
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Estilo CSS personalizado
    st.markdown("""
        <style>
            /* Fundo da barra lateral */
            .css-1d391kg {
                background-color: #f0f2f6;
            }

            /* Cabeçalho */
            .css-hxt7ib {
                color: #31333F;
                font-size: 2rem;
                font-weight: 700;
            }

            /* Título dos grupos */
            .streamlit-expanderHeader {
                font-weight: bold;
                font-size: 16px;
                color: #1f5c8a;
            }

            /* Botão */
            .stButton>button {
                background-color: #1f5c8a;
                color: white;
                font-weight: bold;
            }

            /* Campos de entrada */
            input, .stNumberInput input {
                border-radius: 5px;
                padding: 0.4em;
            }

            /* Métricas */
            .stMetric {
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 0.8em;
                margin: 0.2em 0.5em;
                background-color: #f9f9f9;
            }
        </style>
    """, unsafe_allow_html=True)

