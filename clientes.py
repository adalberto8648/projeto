import csv
import os

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
    if not os.path.exists("clientes.csv"):
        with open("clientes.csv", "w", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Nome", "Idade", "Telefone"])
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
    
    # newline="": Evita que linhas em branco sejam inseridas entre os registros no CSV
    with open("clientes.csv", "a", newline="") as arquivo:
        # csv.writer: escrever dados no CSV
        escritor = csv.writer(arquivo)
        # A função writerow() grava uma linha por vez
        escritor.writerow([nome_completo, idade, telefone_formatado])
    print("\nCliente cadastrado com sucesso")

def listar_clientes(): 
    with open("clientes.csv", "r") as arquivo:
        linhas = arquivo.readlines()
        if linhas:
            print("\n--- Lista de Clientes ---\n")
            for linha in linhas:
                print(linha.strip())
        else:
            print("\nNenhum cliente cadastrado.")
            print("-" * 24 + "\n")
