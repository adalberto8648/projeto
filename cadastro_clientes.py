# 1. Cadastro Simples de Clientes
# Funções básicas: Inserir, listar, e excluir clientes.
# Dados armazenados: Uma lista simples com dicionários para cada cliente.
# Campos: Nome, telefone e e-mail (evite validações avançadas por enquanto).
# Desafios: Usar laços for e while com opções no menu.


# Lista onde vamos armazenar os dados dos clientes temporariamente
clientes = []

# Coletando as informações do cliente
nome_completo = input('Digite aqui o nome do cliente: ')
idade = input('Digite aqui a idade do cliente: ')
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