import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


conexao =sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()

def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()
    
def inserir_dados(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute(f'INSERT INTO clientes (nome, email) VALUES (?, ?)', data)
    conexao.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
   data = (nome, email, id)
   cursor.execute(f'UPDATE clientes SET nome = ?, email = ? WHERE id = ?', data)
   conexao.commit()
   
def excluir_registro(conexao, cursor,id):
   data = (id,)
   cursor.execute(f'DELETE FROM clientes WHERE id = ?', data)
   conexao.commit()
   
# excluir_registro(conexao,cursor, 2)
# atualizar_registro(conexao, cursor, "Lucas balmant", "Lucas@gmail", 1)

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany(f'INSERT INTO clientes (nome, email) VALUES (?, ?)', dados)
    conexao.commit()
    
# dados = {
#     ("Pedro", "Pedro@gmail"),
#     ("Maria", "Maria@gmail"),
#     ("João", "João@gmail"),
#     ("Ana", "Ana@gmail"),
#     ("Carlos", "Carlos@gmail"),
  
# }

# inserir_muitos(conexao, cursor, dados)

def recuperar_cliente(conexao, cursor, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute(f"SELECT * FROM clientes WHERE id = ?", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome").fetchall()

cliente = recuperar_cliente(conexao, cursor, 3)
print(dict(cliente))

clientes = listar_clientes(cursor)
print(clientes)