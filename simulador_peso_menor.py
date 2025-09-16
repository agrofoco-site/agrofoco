# simulador_peso_menor.py
# -*- coding: utf-8 -*-
import streamlit as st
from estilos import set_page_title   # ✅ sem subpasta
from datetime import date

def app():
    set_page_title("Simulador: Peso a Menor")

    st.markdown("Este simulador calcula automaticamente a indenização por peso a menor com base nas entradas abaixo.")

    with st.expander("➕ Novo Cálculo"):
        col1, col2 = st.columns(2)
        with col1:
            clifor = st.text_input("🧾 CLIFOR", "")
            numero_lote = st.text_input("🔢 Nº do Lote", "")
            peso_real = st.number_input("⚖️ Peso Médio Real Entregue (kg)", min_value=0.0, format="%.3f", step=0.01)
            numero_aves = st.number_input("🐔 Nº de Aves Abatidas", min_value=0, step=1)
            valor_pago = st.number_input("💰 Valor Pago pela Integradora (R$)", min_value=0.0, format="%.2f", step=0.01)

        with col2:
            data_abate = st.date_input("🗓️ Data do Abate", value=date.today())
            peso_std = st.number_input("📊 Peso STD (Padrão) (kg)", min_value=0.0, format="%.3f", step=0.01)
            preco_kg = st.number_input("💲 R$ por KG de carne", min_value=0.0, format="%.4f", step=0.0001)
            resultado_bruto = st.number_input("📈 % Resultado Bruto", min_value=0.0, format="%.2f", step=0.01)

        if st.button("Calcular Indenização"):
            # Cálculos
            dif_kg_ave = peso_std - peso_real
            kg_diferenca = dif_kg_ave * numero_aves
            oportunidade = kg_diferenca * preco_kg * (resultado_bruto / 100)
            diferenca_final = oportunidade - valor_pago

            # Resultados
            st.markdown("📄 **Resultado da Simulação**")
            st.write(f"**CLIFOR:** {clifor}")
            st.write(f"**Data de Abate:** {data_abate.strftime('%d/%m/%Y')}")
            st.write(f"**Nº do Lote:** {numero_lote}")

            col1, col2, col3 = st.columns(3)
            col1.metric("📉 Diferença por Ave", f"{dif_kg_ave:.3f} kg")
            col2.metric("📦 KG de Carne Diferença", f"{kg_diferenca:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            col3.metric("💰 Oportunidade de Indenização", f"R$ {oportunidade:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

            st.success(f"💡 Diferença Final (após valor pago): R$ {diferenca_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
