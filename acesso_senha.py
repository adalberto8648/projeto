print("\n---- Acesso ao projeto ----\n")

def acessar_projeto():
    while True:
        nome = "adalberto"
        senha = 123
        acesso_nome = input("Digite o nome: ").lower()
        if acesso_nome == nome:
            while True:
                try:
                    acesso_senha = int(input("Digite a senha: "))
                    if acesso_senha == senha:
                        break
                    else:
                        print("Senha inválida, digite novamente.")
                except ValueError:
                    print("Senha inválida, digite novamente.")
            break
        else:
            print("Nome inválido, digite novamente.")
            continue
    
    print("\n------ Menu Acesso ------")
    print("1 - Cadastro de Clientes")
    print("2 - Números Aleatórios")
    
    while True:
        escolha = input("\nEscolha uma das opções: ")
        if escolha == "1":
            menu_cadastro()
        elif escolha == "2":
            numeros()
        else:
            print("\nOpção inválida, tente novamente")

def menu_cadastro():
    while True:
        print("\n--------- Menu --------")
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
                # Exibe cada linha, removendo espaços antes e depois
                print(linha.strip())
        else:
            print("\nNenhum cliente cadastrado.")
            print("-" * 20)

def numeros():
    quantidade_numeros = int(input("Digite a quantidade de números: "))

    aleatorio = random.randint()


    menor_numero = int(input("Escolha o menor número: "))
    maior_numero = int(input("Escolha o maior número: "))

acessar_projeto()