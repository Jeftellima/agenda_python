import csv

# Função para salvar uma lista no arquivo CSV
def salvar_csv(lista):
    with open('dados.csv', 'w', newline='', encoding='utf-8') as file:
        escrever = csv.writer(file)
        escrever.writerows(lista)

# Função para adicionar dados ao arquivo CSV
def adicionar_dados(dados):
    with open('dados.csv', 'a', newline='', encoding='utf-8') as file:
        escrever = csv.writer(file)
        escrever.writerow(dados)

# Função para ler e retornar os dados do arquivo CSV
def ver_dados():
    dados = []
    try:
        with open('dados.csv', newline='', encoding='utf-8') as file:
            ler_csv = csv.reader(file)
            for linha in ler_csv:
                dados.append(linha)
    except FileNotFoundError:
        # Arquivo não encontrado, cria um arquivo vazio
        salvar_csv([])
    return dados

# Função para remover um dado específico do arquivo CSV
def remover_dados(telefone):
    nova_lista = []
    with open('dados.csv', 'r', newline='', encoding='utf-8') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            if telefone not in linha:  # Remove a linha que contém o telefone
                nova_lista.append(linha)

    # Atualiza o arquivo com a nova lista
    salvar_csv(nova_lista)

# Função para atualizar dados no arquivo CSV
def atualizar_dados(dados_novos):
    telefone_antigo = dados_novos[2]  # O telefone atual é usado como identificador
    nova_lista = []

    with open('dados.csv', 'r', newline='', encoding='utf-8') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            if telefone_antigo in linha:  # Encontrou a linha a ser atualizada
                print(f"Atualizando dados: {linha} -> {dados_novos}")  # Log para depuração
                nova_lista.append(dados_novos)
            else:
                nova_lista.append(linha)

    # Atualiza o arquivo com a nova lista
    salvar_csv(nova_lista)


# Função para pesquisar dados no arquivo CSV
def pesquisar_dados(telefone):
    dados = []
    try:
        with open('dados.csv', newline='', encoding='utf-8') as file:
            ler_csv = csv.reader(file)
            for linha in ler_csv:
                if telefone in linha:  # Verifica se o telefone está na linha
                    dados.append(linha)
    except FileNotFoundError:
        # Caso o arquivo não exista, retorna uma lista vazia
        return []
    return dados
