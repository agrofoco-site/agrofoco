# criar_tabela_dados.py
import sqlite3

conn = sqlite3.connect("AGROFOCO.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS dados_cadastro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    usuario TEXT
)
""")

conn.commit()
conn.close()
print("Tabela criada com sucesso ✅")
