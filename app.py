import tkinter as tk
from tkinter import ttk
import psycopg2


class App:
    def __init__(self, master):

        self.master = master
        self.master.title("Gerenciador de Estoque de Adega")

        self.master.resizable(False, False)

        # # Conexão com o banco de dados PostgreSQL
        # self.conn = psycopg2.connect(
        #     host="hostname",
        #     database="database_name",
        #     user="username",
        #     password="password"
        # )
        # self.cur = self.conn.cursor()

        # Criação das abas
        self.tabControl = ttk.Notebook(self.master)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text="Adicionar Produto")
        self.tabControl.add(self.tab2, text="Retirar Produto")
        self.tabControl.add(self.tab3, text="Consultar Produto")
        self.tabControl.pack(expand=1, fill="both")

        # Estilizando
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 8), foreground="black")
        style.configure("TButton", font=("Helvetica", 8), foreground="black")

        # Conteúdo da aba "Adicionar Produto"
        ttk.Label(self.tab1, text="Código do Produto:", style="TLabel").grid(
            row=0, column=0, sticky="e", padx=10, pady=10)
        self.produto_codigo = ttk.Entry(self.tab1)
        self.produto_codigo.grid(
            row=0, column=1, sticky="ew", padx=10, pady=10)

        ttk.Label(self.tab1, text="Nome do Produto:", style="TLabel").grid(
            row=1, column=0, sticky="e", padx=10, pady=10)
        self.produto_nome = ttk.Entry(self.tab1)
        self.produto_nome.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

        ttk.Label(self.tab1, text="Valor:", style="TLabel").grid(
            row=2, column=0, sticky="e", padx=10, pady=10)
        self.produto_valor = ttk.Entry(self.tab1)
        self.produto_valor.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

        ttk.Label(self.tab1, text="Quantidade:", style="TLabel").grid(
            row=3, column=0, sticky="e", padx=10, pady=10)
        self.produto_quantidade = ttk.Entry(self.tab1)
        self.produto_quantidade.grid(
            row=3, column=1, sticky="ew", padx=10, pady=10)

        ttk.Label(self.tab1, text="Categoria:", style="TLabel").grid(
            row=4, column=0, sticky="e", padx=10, pady=10)
        self.produto_categoria = ttk.Combobox(
            self.tab1, values=["Vinho", "Whisky", "Vodka"])
        self.produto_categoria.grid(
            row=4, column=1, sticky="ew", padx=10, pady=10)

        ttk.Button(self.tab1, text="Adicionar", command=self.adicionar_produto,
                   style="TButton").grid(row=5, columnspan=2,
                                         sticky="e", padx=10, pady=10)

        # Conteúdo da aba "Retirar Produto"
        ttk.Label(self.tab2, text="Retirar por:").grid(
            row=0, column=0, sticky="e", padx=10, pady=10)
        self.tipo_retirada = ttk.Combobox(self.tab2, values=["Nome", "Código"])
        self.tipo_retirada.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

        ttk.Label(self.tab2, text="Parâmetro:").grid(
            row=1, column=0, sticky="e", padx=10, pady=10)
        self.valor_retirada = ttk.Entry(self.tab2)
        self.valor_retirada.grid(
            row=1, column=1, sticky="ew", padx=10, pady=10)

        ttk.Label(self.tab2, text="Quantidade:").grid(
            row=2, column=0, sticky="e", padx=10, pady=10)
        self.quantidade_produto_retirar = ttk.Entry(self.tab2)
        self.quantidade_produto_retirar.grid(
            row=2, column=1, sticky="ew", padx=10, pady=10)

        ttk.Button(self.tab2, text='Retirar', command=self.retirar_produto).grid(
            row=3, columnspan=2, sticky="e", padx=10, pady=10)

        # Conteúdo da aba "Consultar Produto"
        ttk.Label(self.tab3, text="Consultar por:").grid(
            row=0, column=0, sticky="e", padx=10, pady=10)
        self.consulta_tipo = ttk.Combobox(self.tab3, values=["Nome", "Código"])
        self.consulta_tipo.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

        ttk.Label(self.tab3, text="Filtro:").grid(
            row=1, column=0, sticky="e", padx=10, pady=10)
        self.consulta_filtro = ttk.Combobox(
            self.tab3, values=["Inicie com", "Contenha", "Seja igual"])
        self.consulta_filtro.grid(
            row=1, column=1, sticky="ew", padx=10, pady=10)

        ttk.Label(self.tab3, text="Ordenar por:").grid(
            row=2, column=0, sticky="e", padx=10, pady=10)
        self.consulta_ordem = ttk.Combobox(
            self.tab3, values=["Quantidade", "Valor", "Ordem alfabética"])
        self.consulta_ordem.grid(
            row=2, column=1, sticky="ew", padx=10, pady=10)

        ttk.Label(self.tab3, text="Parâmetro:").grid(
            row=3, column=0, sticky="e", padx=10, pady=10)
        self.consulta_valor = ttk.Entry(self.tab3)
        self.consulta_valor.grid(
            row=3, column=1, sticky="ew", padx=10, pady=10)

        ttk.Button(self.tab3, text="Consultar", command=self.consultar_produto).grid(
            row=4, columnspan=2, sticky="e", padx=10, pady=10)

        # Espaço para a tabela de resultados
        self.resultados_frame = ttk.Frame(self.tab3)
        self.resultados_frame.grid(row=5, columnspan=2)

    def adicionar_produto(self):
        codigo = int(self.produto_codigo.get())
        nome = self.produto_nome.get()
        valor = float(self.produto_valor.get())
        quantidade = int(self.produto_quantidade.get())
        categoria = self.produto_categoria.get()

        # Verifica se o produto já existe no banco de dados
        query = "SELECT * FROM produtos WHERE codigo=%s"
        values = (codigo,)
        self.cur.execute(query, values)
        if (self.cur.rowcount == 0):
            # Insere o produto no banco de dados
            query = "INSERT INTO produtos (codigo, nome, valor, quantidade, categoria) VALUES (%s,%s,%s,%s,%s)"
            values = (codigo, nome, valor, quantidade, categoria)
            self.cur.execute(query, values)
            self.conn.commit()
            print("Produto adicionado com sucesso")
        else:
            row = self.cur.fetchone()
            # Atualiza a quantidade do produto no banco de dados
            query = "UPDATE produtos SET quantidade=%s WHERE codigo=%s"
            values = (row[3] + quantidade, codigo)
            self.cur.execute(query, values)
            self.conn.commit()
            print("Quantidade do produto atualizada com sucesso")

    def retirar_produto(self):
        tipo = self.tipo_retirada.get()
        valor = self.valor_retirada.get()
        quantidade = int(self.quantidade_produto_retirar.get())

        if tipo == "Nome":
            query = "SELECT * FROM produtos WHERE nome=%s"
            values = (valor,)
        elif tipo == "Código":
            query = "SELECT * FROM produtos WHERE codigo=%s"
            values = (valor,)
        else:
            print("Tipo de retirada inválido")
            return

        self.cur.execute(query, values)
        if (self.cur.rowcount == 0):
            print("Produto não encontrado")
            return
        else:
            row = self.cur.fetchone()
            if row[3] < quantidade:
                print("Quantidade insuficiente no estoque")
                return
            else:
                print(
                    f"Código: {row[0]}, Nome: {row[1]}, Valor: {row[2]}, Quantidade: {quantidade}, Categoria: {row[4]}")
                print(f"Valor total: {row[2] * quantidade}")

        # Atualiza a quantidade do produto no banco de dados
        query = "UPDATE produtos SET quantidade=%s WHERE codigo=%s"
        values = (row[3] - quantidade, row[0])
        try:
            self.cur.execute(query, values)
            self.conn.commit()
            print("Produto retirado com sucesso")
        except Exception as e:
            print(e)

    def consultar_produto(self):
        tipo = self.consulta_tipo.get()
        filtro = self.consulta_filtro.get()
        valor = self.consulta_valor.get()
        ordem = self.consulta_ordem.get()

        if tipo == "Nome":
            if filtro == "Inicie com":
                query = "SELECT * FROM produtos WHERE nome LIKE %s"
                values = (valor + "%",)
            elif filtro == "Contenha":
                query = "SELECT * FROM produtos WHERE nome LIKE %s"
                values = ("%" + valor + "%",)
            elif filtro == "Seja igual":
                query = "SELECT * FROM produtos WHERE nome=%s"
                values = (valor,)
            else:
                print("Filtro inválido")
                return
        elif tipo == "Código":
            if filtro == "Seja igual":
                query = "SELECT * FROM produtos WHERE codigo=%s"
                values = (valor,)
            else:
                print("Filtro inválido para consulta por código")
                return
        else:
            print("Tipo de consulta inválido")
            return

        if ordem == "Quantidade":
            query += " ORDER BY quantidade"
        elif ordem == "Valor":
            query += " ORDER BY valor"
        elif ordem == "Ordem alfabética":
            query += " ORDER BY nome"

        try:
            self.cur.execute(query, values)
            if (self.cur.rowcount == 0):
                print("Nenhum produto encontrado")
            else:
                rows = self.cur.fetchall()

                # Criação da tabela
                self.tree = ttk.Treeview(self.tab3, columns=(
                    "Código", "Nome", "Valor", "Quantidade", "Categoria"), show="headings")
                self.tree.heading("Código", text="Código")
                self.tree.heading("Nome", text="Nome")
                self.tree.heading("Valor", text="Valor")
                self.tree.heading("Quantidade", text="Quantidade")
                self.tree.heading("Categoria", text="Categoria")

                for row in rows:
                    self.tree.insert("", tk.END, values=row)

                self.tree.grid(row=5, columnspan=2)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
