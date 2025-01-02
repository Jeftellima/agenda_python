from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from dados import *

# Cores
co0 = "#f0f3f5"  # Preta
co1 = "#f0f3f5"  # Cinza / grey
co2 = "#feffff"  # Branca
co3 = "#38576b"  # Preta / black
co4 = "#403d3d"  # Letra
co5 = "#6f9fbd"  # Azul
co6 = "#ef5350"  # Vermelha
co7 = "#93cd95"  # Verde

# Criando janela
janela = Tk()
janela.title("Programa Agenda Telefônica")
janela.geometry('500x450')
janela.configure(background=co1)
janela.resizable(width=False, height=False)

# Estilo do tema
style = ttk.Style(janela)
style.theme_use("clam")

# Frames
frame_cima = Frame(janela, width=500, height=50, bg=co3, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=500, height=150, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_tabela = Frame(janela, width=500, height=248, bg=co2, relief="flat")
frame_tabela.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)

# Configurando frame superior
l_nome = Label(frame_cima, text='Cadastro de Contatos', anchor=NE, font=('arial 20 bold'), bg=co3, fg=co1)
l_nome.place(x=3, y=5)

l_linha = Label(frame_cima, text='', width=500, anchor=NE, font=('arial 1'), bg=co2, fg=co1)
l_linha.place(x=0, y=46)

global tree

def mostrar_dados():
    global tree

    dados_h = ['Nome', 'Sexo', 'Telefone', 'Email']

    dados = ver_dados()

    # Criando o Treeview com barras de rolagem
    tree = ttk.Treeview(frame_tabela, selectmode="extended", columns=dados_h, show="headings")

    # Barras de rolagem
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)

    # Configurações
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Inserindo dados
    for item in dados:
        tree.insert('', 'end', values=item)

    # Configurando cabeçalhos e colunas
    for col, header in enumerate(dados_h):
        tree.heading(col, text=header, anchor=NW)
        tree.column(col, width=120, anchor='nw')

    # Grid da Treeview e Scrollbars
    tree.grid(column=0, row=0, sticky='nswe')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

mostrar_dados()
    

# Função para inserir dados
def inserir():
    nome = e_nome.get()
    sexo = c_genero.get()
    telefone = e_tel.get()
    email = e_email.get()

    dados = [nome, sexo, telefone, email]

    if nome == '' or sexo == '' or telefone == '' or email == '':
        messagebox.showwarning('Dados', 'Por favor, preencha todos os campos.')
    else:
        adicionar_dados(dados)
        messagebox.showinfo('Dados', 'Dados adicionados com sucesso.')

        e_nome.delete(0, 'end')
        c_genero.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_email.delete(0, 'end')
        mostrar_dados()

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']  # Corrigido o nome da variável

        nome = tree_lista[0]
        sexo = tree_lista[1]
        telefone = str(tree_lista[2])
        email = tree_lista[3]

        e_nome.insert(0, nome)  # Corrigido para mostrar o valor da variável
        c_genero.insert(0, sexo)  # Corrigido para mostrar o valor da variável
        e_tel.insert(0, telefone)  # Corrigido para mostrar o valor da variável
        e_email.insert(0, email)  # Corrigido para mostrar o valor da variável

        def confirmar():
            nome = e_nome.get()
            sexo = c_genero.get()
            telefone = e_tel.get()
            email = e_email.get()

            dados = [nome, sexo, telefone, email]

            if nome == '' or sexo == '' or telefone == '' or email == '':
                messagebox.showwarning('Dados', 'Por favor, preencha todos os campos.')
                return

            # Atualizar os dados na fonte de dados (banco de dados ou lista)
            atualizar_dados(dados)

            # Remover o item antigo da árvore
            for item in tree.get_children():
                if tree.item(item, 'values')[2] == telefone:  # Identifica o item pelo telefone
                    tree.delete(item)
                    break

            # Adicionar o novo item com os dados atualizados
            tree.insert('', 'end', values=dados)

            messagebox.showinfo('Dados', 'Dados foram atualizados com sucesso.')

            # Limpar os campos
            e_nome.delete(0, 'end')
            c_genero.set('')  # Resetar o valor do combobox
            e_tel.delete(0, 'end')
            e_email.delete(0, 'end')

            # Fechar o botão de confirmação
            b_confirmar.destroy()

            # Atualizar a tabela
            mostrar_dados()


        b_confirmar = Button(frame_baixo, command=confirmar, text='Confirmar', width=10, font=('Ivy 8 bold'), bg=co5, fg=co4, relief=RAISED, overrelief=RIDGE)
        b_confirmar.place(x=290, y=110)
    except:
        messagebox.showwarning('Dados', 'Por favor selecione uma informação na tabela')


def deletar():
    try:
        item_selecionado = tree.focus()
        valores = tree.item(item_selecionado, 'values')
        telefone = valores[2]  # O telefone é usado como identificador
        remover_dados(telefone)
        messagebox.showinfo('Dados', 'Registro removido com sucesso.')
        for widget in frame_tabela.winfo_children():
            widget.destroy()

        mostrar_dados()
    except IndexError:
        messagebox.showwarning('Erro', 'Por favor, selecione um item para remover.')

def procurar():
    telefone = e_procurar.get()
    dados = pesquisar_dados(telefone)
    tree.delete(*tree.get_children())
    for item in dados:
        tree.insert('', 'end', values=item)

    e_procurar.delete(0, 'end')



# Configurando frame inferior
l_nome = Label(frame_baixo, text='Nome*', anchor=NE, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=25, justify='left', font=('', 10), highlightthickness=1)
e_nome.place(x=80, y=10)

l_genero = Label(frame_baixo, text='Gênero*', anchor=NE, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_genero.place(x=10, y=40)
c_genero = ttk.Combobox(frame_baixo, width=27)
c_genero['value'] = ('', 'F', 'M')
c_genero.place(x=80, y=40)

l_tel = Label(frame_baixo, text='Telefone*', anchor=NE, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_tel.place(x=10, y=70)
e_tel = Entry(frame_baixo, width=25, justify='left', font=('', 10), highlightthickness=1)
e_tel.place(x=80, y=70)

l_email = Label(frame_baixo, text='Email*', anchor=NE, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_email.place(x=10, y=100)
e_email = Entry(frame_baixo, width=25, justify='left', font=('', 10), highlightthickness=1)
e_email.place(x=80, y=100)

b_procurar = Button(frame_baixo, command=procurar, text='Procurar', font=('Ivy 8 bold'), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
b_procurar.place(x=290, y=10)
e_procurar = Entry(frame_baixo, width=16, justify='left', font=('', 11), highlightthickness=1)
e_procurar.place(x=357, y=11)

b_ver = Button(frame_baixo, command=mostrar_dados, text='Ver Dados', width=10, font=('Ivy 8 bold'), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
b_ver.place(x=320, y=40)

b_adicionar = Button(frame_baixo, command=inserir, text='Adicionar', width=10, font=('Ivy 8 bold'), bg=co5, fg=co4, relief=RAISED, overrelief=RIDGE)
b_adicionar.place(x=410, y=70)

b_atualizar = Button(frame_baixo, command=atualizar, text='Atualizar', width=10, font=('Ivy 8 bold'), bg=co7, fg=co4, relief=RAISED, overrelief=RIDGE)
b_atualizar.place(x=410, y=100)

b_deletar = Button(frame_baixo, command=deletar, text='Deletar', width=10, font=('Ivy 8 bold'), bg=co6, fg=co4, relief=RAISED, overrelief=RIDGE)
b_deletar.place(x=410, y=40)

# Iniciando a interface
janela.mainloop()