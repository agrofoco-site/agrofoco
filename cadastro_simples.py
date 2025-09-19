import streamlit as st
import sqlite3
import pandas as pd

def get_connection():
    return sqlite3.connect("AGROFOCO.db")

def app():
    st.title("📋 Cadastro Simples com Edição e Exclusão Inline")

    if "logado" not in st.session_state or not st.session_state.logado:
        st.warning("⚠️ Você precisa estar logado para acessar esta página.")
        return

    usuario_logado = st.session_state.usuario

    # Seção de Cadastro no Topo
    with st.form("novo_registro"):
        st.subheader("➕ Novo Cadastro")
        nome_novo = st.text_input("Nome")
        idade_novo = st.number_input("Idade", min_value=0, step=1)

        if st.form_submit_button("Cadastrar"):
            if nome_novo.strip():
                conn = get_connection()
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO dados_cadastro (nome, idade, usuario)
                    VALUES (?, ?, ?)
                """, (nome_novo.strip(), idade_novo, usuario_logado))
                conn.commit()
                conn.close()
                st.success("✅ Novo registro cadastrado!")
                st.rerun()
            else:
                st.warning("⚠️ O campo nome é obrigatório.")

    st.markdown("---")

    # Consulta os dados
    conn = get_connection()
    cur = conn.cursor()

    if usuario_logado == "admin":
        cur.execute("SELECT id, nome, idade, usuario FROM dados_cadastro")
        colunas = ["id", "nome", "idade", "usuario"]
    else:
        cur.execute("SELECT id, nome, idade FROM dados_cadastro WHERE usuario = ?", (usuario_logado,))
        colunas = ["id", "nome", "idade"]

    dados = cur.fetchall()
    conn.close()

    if not dados:
        st.info("Nenhum dado cadastrado ainda.")
        return

    df_original = pd.DataFrame(dados, columns=colunas)
   # df_original["Selecionar"] = False  # coluna para checkbox
    df_original.insert(0, "Selecionar", False)  # insere como primeira coluna


    st.subheader("📄 Registros (clique para editar ou marcar para excluir)")

    edited_df = st.data_editor(
        df_original,
        num_rows="dynamic",
        use_container_width=True,
        key="editor",
        disabled=["id", "usuario"] if "usuario" in df_original.columns else ["id"],
    )

    # Edição
    if not df_original.drop(columns=["Selecionar"]).equals(edited_df.drop(columns=["Selecionar"])):
        if st.button("💾 Salvar alterações"):
            conn = get_connection()
            cur = conn.cursor()
            for _, row in edited_df.iterrows():
                if usuario_logado == "admin":
                    cur.execute("""
                        UPDATE dados_cadastro
                        SET nome = ?, idade = ?, usuario = ?
                        WHERE id = ?
                    """, (row["nome"], row["idade"], row.get("usuario", usuario_logado), row["id"]))
                else:
                    cur.execute("""
                        UPDATE dados_cadastro
                        SET nome = ?, idade = ?
                        WHERE id = ? AND usuario = ?
                    """, (row["nome"], row["idade"], row["id"], usuario_logado))
            conn.commit()
            conn.close()
            st.success("✅ Alterações salvas com sucesso!")
            st.rerun()
    else:
        st.info("Faça alterações na tabela acima para ativar o botão de salvar.")

    # Exclusão
    ids_para_deletar = edited_df[edited_df["Selecionar"] == True]["id"].tolist()
    if ids_para_deletar:
        if st.button("🗑️ Excluir Selecionados"):
            conn = get_connection()
            cur = conn.cursor()

            for id in ids_para_deletar:
                if usuario_logado == "admin":
                    cur.execute("DELETE FROM dados_cadastro WHERE id = ?", (id,))
                else:
                    cur.execute("DELETE FROM dados_cadastro WHERE id = ? AND usuario = ?", (id, usuario_logado))

            conn.commit()
            conn.close()
            st.success(f"🗑️ {len(ids_para_deletar)} registro(s) excluído(s) com sucesso!")
            st.rerun()
