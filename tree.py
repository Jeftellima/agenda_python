from tkinter import ttk
from dados import ver_dados  # Certifique-se de importar a função ver_dados

def setup_tree(frame_tabela):
    # Definindo as colunas
    dados_h = ['Nome', 'Sexo', 'Telefone', 'Email']

    # Obtendo os dados do CSV
    dados = ver_dados()  # Função que retorna os dados do arquivo CSV

    # Criando a treeview
    tree = ttk.Treeview(frame_tabela, selectmode="extended", columns=dados_h, show="headings")

    # Configurando a scrollbar vertical e horizontal
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Adicionando a tree ao layout
    tree.grid(column=0, row=0, sticky='nswe')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    # Cabeçalhos da árvore
    for col, header in enumerate(dados_h):
        tree.heading(col, text=header, anchor="nw")
        tree.column(col, width=120, anchor='nw')

    # Inserindo os dados na árvore
    for item in dados:
        tree.insert('', 'end', values=item)
