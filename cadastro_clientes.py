# 1. Cadastro Simples de Clientes
# Funções básicas: Inserir, listar, e excluir clientes.
# Dados armazenados: Uma lista simples com dicionários para cada cliente.
# Campos: Nome, telefone e e-mail (evite validações avançadas por enquanto).
# Desafios: Usar laços for e while com opções no menu.

# ("a") adição, append, insere dados 
# ("r") abre o arquivo padrão
# ("w") abre o arquivo para alterar

def cadastrar_clientes():
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
        try:
            idade = int(input("Digite aqui a idade do cliente: "))
            if idade > 0:
                break
            else:
                print("Digite apenas números maiores que zero para a idade do cliente")
        except ValueError:
            print('Digite apenas números para a idade do cliente')

    while True:
        telefone = input("Digite aqui o telefone do cliente: ")
        if len(telefone) != 11 or not telefone.isdigit():
            print('O telefone deve ter 11 números. Tente novamente')
            continue # aqui é pra continuar e voltar no início
        telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
        break

    # with fechado automaticamente quando terminarmos de usá-lo
    # open abre o arquivo no modo escolhido
    # adição ("a") de append, insere dando seguência 
    with open("clientes.txt", "a") as arquivo:
        # escrevendo os dados no arquivo
        arquivo.write(f"Nome: {nome_completo}\n")
        arquivo.write(f"Idade: {idade}\n")
        arquivo.write(f"Telefone: {telefone_formatado}\n")
        arquivo.write(f"-" * 25 + "\n")
    print("\nCliente cadastrado com sucesso")

def listar_clientes():
    # with fechado automaticamente quando terminarmos de usá-lo
    # open abre o arquivo no modo escolhido
    # ("r") abre o arquivo 
    with open("clientes.txt", "r") as arquivo:

        linhas = arquivo.readlines()

        if linhas:
            print("\n--- Lista de Clientes ---\n")

            for linha in linhas:
                # Exibe cada linha, removendo espaços antes e depois
                print(linha.strip())
        else:
            print("\nNenhum cliente cadastrado.")
            print("-" * 20)

while True:
    print("\n---------- Menu ---------")
    print("1 - Cadastrar Clientes")
    print("2 - Listar Clientes")
    print("3 - Sair")
    escolha = input("\nEscolha uma opção: ")
    print("-" * 24)
    
    if escolha == "1":
        cadastrar_clientes()

    elif escolha == "2":
        listar_clientes()

    elif escolha == "3":
            print("Saindo ...")
            break
    else:
        print("\nOpção inválida. Tente novamente.")


