from database.db import database

from models.livros import Livro

class livroController:
    def __init__(self, db_config):
        self.db = database(
      db_config["dbname"]
      db_config["user"]
      db_config["password"]
      db_config["host"]
      db_config["port"]
     )
    self.criar_tabelas_livro()
    self.view = livroView()

    def criar_tabelas_livro(self):
        con = self.db.conectar()
        if conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS livro (
                    id SERIAL PRIMARY KEY,
                    titulo VARCHAR(255) NOT NULL,
                    autor VARCHAR(255) NOT NULL,
                    ano_publicacao INTEGER NOT NULL,
                    isbn VARCHAR(255) NOT NULL
                )
            """)
            conn.commit()
            conn.close()
        print("Tabelas criadas com sucesso!")
    else:
        print("Erro ao conectar ao banco de dados.")

def listar_livros(self):
    #self.view.mostrar_livro(livros)
    conn = self.db.conectar()
    livros = []
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT id,titulo, autor. ano_publicacao, isbn FROM livro ORDER BY id;")
        for linha in cur.fetchall():
            livros.append(livro(*linha))
            cur.close()
            cur.close()
        return livros 
           