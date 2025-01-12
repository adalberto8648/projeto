# 1. Cadastro Simples de Clientes
# Funções básicas: Inserir, listar, e excluir clientes.
# Dados armazenados: Uma lista simples com dicionários para cada cliente.
# Campos: Nome, telefone e e-mail (evite validações avançadas por enquanto).
# Desafios: Usar laços for e while com opções no menu.


# Lista onde vamos armazenar os dados dos clientes temporariamente
clientes = []

# Coletando as informações do cliente
while True:
    # Inserindo nome e tornando tudo minúsculo
    nome_completo = input("Digite aqui o nome do cliente: ").lower()
    # Removendo espaços antes e depois e se não está vazio
    if nome_completo.strip() == "":
        print("Campo em branco, digite o nome do cliente.")
    # Eliminando espaços internos e vefiicando se tem apenas letras
    elif nome_completo.replace(" " , "").isalpha():
        break
    else:
        print("Digite apenas letras para o nome do cliente.")

while True:
    # Verificando se existe erro, colocando texto onde seria apenas números
    try:
        # Inserindo idade do cliente
        idade = int(input('Digite aqui a idade do cliente: '))
        # Removendo espaços antes e depois e se não está vazio
        if idade > 0:
            break
        else:
            print('Digite apenas números maiores que zero para a idade do cliente')
    # Retornando a mensagem
    except ValueError:
        print('Digite apenas números para a idade do cliente')


telefone = input('Digite aqui o telefone do cliente: ')

# Armazenando as informações em um dicionário
cliente = {
    'Nome' : nome_completo,
    'Idade' : idade,
    'Telefone' : telefone
}

# Adicionando o dicionário de cliente na lista de clientes provisório
clientes.append(cliente)

# Exibindo as informações do cliente cadastrado

print('\nCliente cadastrado com sucesso')
print(f'Nome: {cliente['Nome']}')
print(f'Idade: {cliente["Idade"]}')
print(f'Telefone: {cliente["Telefone"]}')