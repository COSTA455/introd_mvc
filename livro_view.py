'''class livroView:
    def exibir_livros(self, livros):
        print(livros)
        # Lógica para exibir os livros

    def mostrar_livro(self, livro):  
        for livro in livro
         self.mostrar_livro(livro)
     
'''

import tkinter as tk
from tkinter import ttk messagebox
from controllers.livro_controller import LivroController

class LivroView:
    def __init__(self, controller):
        self.controller = controller
        self._show_livros_tela()

@staticmethod
 def iniciar_login_banco():
    def conectar():
        db_config = {
          "dbname": db_name_entry.get(), 
            "user": user_entry.get(),
            "password": password_entry.get(),
            "host": host_entry.get(),
            "porta": port_entry.get()
            }
            
        try:

            controller = LivroController(db_config)
            login_win.destroy()
            LivroView(controller)
        except Exception as e:
            messagebox.showerror(f"Erro ao conectar ao banco de dados\n {e}")
       
    
    login_win = tk.Tk()
    login_win.title("Conectar ao banco de dados")
    login_win.geometry("300x200")

    tk.Label(login_win, texto="host:").pack(pady=2)
    host_entry = tk.Entry(login_win)
    host_entry.pack()

    tk.Label(login_win, texto="porta:").pack(pady=2)
    db_port_entry = tk.Entry(login_win)
    db_port_entry.pack()

    tk.Label(login_win, texto="dbname:").pack(pady=2)
    db_name_entry = tk.Entry(login_win)
    db_name_entry.pack()

    tk.Label(login_win, texto="user:").pack(pady=2)
    db_user_entry = tk.Entry(login_win)
    db_user_entry.pack()

    tk.Label(login_win, texto="senha:").pack(pady=2)
    db_password_entry = tk.Entry(login_win)
    db_password_entry.pack()
     
    tk.Button(login_win, text="Conectar", command=conectar).pack(pady=10)
    login_win.mainloop() 
    

    def _show_livros_tela(self):
       livros = self.controller.listar_livros()
       win = tk.Tk()
       win.title("Livros cadastrados")
       win.geometry("700x400")
       
       colums = ("id", "titulo", "autor", "ano_publicacao", "isbn")
       tree = ttk.Treeview(win, columns=colums, show="headings")
       tree.pack()

       for col in colums:
           tree.heading(col, text=col.capitalize())
           tree.column(col, width=120)

        for livro in livros:
            tree.insert("", tk.END, values=(livro.id, livro.titulo, livro.autor, livro.ano_publicacao, livro.isbn))
        tree.pack(except=true, fill="both") 

        win.mainloop()
           