print("\n---- Acesso ao projeto ----\n")

def acessar_projeto():
    nome = "adalberto"
    senha = "123"
    while True:
        acesso_nome = input("Digite o nome: ")
        if acesso_nome == nome:
            while True:
                acesso_senha = input("Digite a senha: ")
                if acesso_senha == senha:
                    print("Acesso permitido.")
                    break
                print("Senha inválida, digite novamente.")
            break
        else:
            print("Nome inválido, digite novamente.")

    while True:
        print("\n----- Menu Projeto -----")
        print("1 - Clientes")
        print("2 - Fornecedor")
        print("3 - Produtos")
        escolha = input("\nEscolha uma das opções: ")
        print("-" * 24 + "\n")
        
        if escolha == "1":
            menu_clientes()
        elif escolha == "2":
            menu_fornecedores()
        elif escolha == "3":
            menu_produtos()
        else:
            print("Opção inválida, tente novamente\n")
    
def menu_clientes():
    while True:
        print("\n----- Menu clientes -----")
        print("1 - Cadastrar Clientes")
        print("2 - Listar Clientes")
        print("3 - Menu Projeto")
        escolha = input("\nEscolha uma opção: ")
        print("-" * 24 + "\n")
        
        if escolha == "1":
            cadastrar_clientes()
        elif escolha == "2":
            listar_clientes()
        elif escolha == "3":
            print("Acessando -> Menu Projeto ...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

def cadastrar_clientes():
    while True:
        # Inserindo nome e tornando tudo minúsculo
        nome_completo = input("Digite aqui o nome do cliente: ").strip()
        if not nome_completo:
            print("Campo em branco, digite o nome do cliente.")
            continue
        else:
            break
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
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(f"Nome: {nome_completo}\n")
        arquivo.write(f"Idade: {idade}\n")
        arquivo.write(f"Telefone: {telefone_formatado}\n")
        arquivo.write(f"-" * 25 + "\n")
    print("\nCliente cadastrado com sucesso")

def listar_clientes(): 
    with open("clientes.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        if linhas:
            print("\n--- Lista de Clientes ---\n")
            for linha in linhas:
                print(linha.strip())
        else:
            print("\nNenhum cliente cadastrado.")
            print("-" * 24 + "\n")

def menu_fornecedores():
    while True:
        print("\n--- Menu Fornecedores ---")
        print("1 - Cadastrar Fornecedors")
        print("2 - Listar Fornecedores")
        print("3 - Menu Projeto")
        escolha = input("\nEscolha uma opção: ")
        print("-" * 24 + "\n")

        if escolha == "1":
            cadastrar_fornecedores()
        elif escolha == "2":
            listar_fornecedores()
        elif escolha == "3":
            print("Acessando -> Menu Projeto ...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

def cadastrar_fornecedores():
    while True:
        codigo_fornecedor = input("Digite o código do fornecedor: ").strip()
        if not codigo_fornecedor:
            print("Campo em branco, digite o código do fornecedor.")
        elif " " in codigo_fornecedor:
            print("O código do fornecedor não pode ter espaços.")
        else:
            break
    while True:
        nome_fornecedor = input("Digite o nome do fornecedor: ").strip()
        if not nome_fornecedor:
            print("Campo em branco, digite o nome do fornecedor.")
        else:
            break
    with open("fornecedores.txt", "a") as arquivo:
        arquivo.write(f"Codigo: {codigo_fornecedor}\n")
        arquivo.write(f"Nome: {nome_fornecedor}\n")
        arquivo.write(f"-" * 25 + "\n")
    print("\nFornecedor cadastrado com sucesso")
    
def listar_fornecedores():
    with open("fornecedores.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        if linhas:
            print("\n--Lista de Fornecedores--\n")
            for linha in linhas:
                print(linha.strip())
        else:
            print("\nNenhum Fornecedor encontrado.")
            print("-" * 24 + "\n")

def menu_produtos():
    while True:
        print("\n---- Menu Produtos ----")
        print("1 - Cadastrar Produtos")
        print("2 - Listar Produtos")
        print("3 - Menu Projeto")
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            cadastrar_produtos()
        elif escolha == "2":
            listar_produtos()
        elif escolha == "3":
            print("Acessando -> Menu Projeto ...")
            break
        else:
            print("\nCódigo inválido, digite novamente")

def cadastrar_produtos():
    while True:
        codigo_produto = input("Digite o código do produto: ").strip()
        if not codigo_produto:
            print("Campo em branco, digite o código do produto.")
        elif " " in codigo_produto:
            print("O código do produto não pode ter espaços.")
        else:
            break
    while True:
        nome_produto = input("Digite o nome do produto: ").strip()
        if not nome_produto:
            print("Campo em branco, digite o nome do produto.")
        else:
            break
    with open("produtos.txt", "a") as arquivo:
        arquivo.write(f"Codigo: {codigo_produto}\n")
        arquivo.write(f"Nome: {nome_produto}\n")
        arquivo.write(f"-" * 24 + "\n")
    print("\nProduto cadastrado com sucesso")

def listar_produtos():
    with open("produtos.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        if linhas:
            print("\n----- Lista de produtos -----")
            for linha in linhas:
                print(linha.strip())
        else:
            print("\nNenhum Produto encontrado.")
            print("-" * 24 + "\n")
            
acessar_projeto()