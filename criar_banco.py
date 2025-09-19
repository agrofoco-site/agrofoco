import sqlite3
import bcrypt

conn = sqlite3.connect("AGROFOCO.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)
""")

usuarios = [
    ("admin", "6881"),
    ("antonio", "818060"),
    ("jean", "123456")
]

for user, pwd in usuarios:
    hash_senha = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()
    try:
        cur.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (user, hash_senha))
    except sqlite3.IntegrityError:
        pass  # se já existe, ignora

conn.commit()
conn.close()

print("Banco AGROFOCO.db criado com usuários iniciais ✅")
