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
            escritor.writerow(["Codigo", "Nome", "Idade", "Telefone"])
    while True:
        codigo_cliente = input("Digite o código do cliente: ")
        if codigo_cliente and codigo_cliente.isdigit():
            break
        print("Para o código do cliente digite apenas números.")
    while True:
        nome_completo = input("Digite o nome do cliente: ").strip()
        if nome_completo:
            break
        print("Campo em branco, digite o nome do cliente.")
    while True:
        try:
            idade = int(input("Digite a idade do cliente: "))
            if idade > 0:
                break
            else:
                print("Digite números maiores que zero para a idade do cliente")
        except ValueError:
            print('Digite apenas números para a idade do cliente')
    while True:
        telefone = input("Digite o telefone do cliente: ")
        if len(telefone) == 11 and telefone.isdigit():
            telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
            break
        print('O telefone deve ter DDD + 9 números. Ex.99999999999.')
    with open("clientes.csv", "a", newline="") as arquivo:
        # csv.writer: escrever dados no CSV
        escritor = csv.writer(arquivo)
        # A função writerow() grava uma linha por vez
        escritor.writerow([codigo_cliente, nome_completo, idade, telefone_formatado])
    print("\nCliente cadastrado com sucesso")

def listar_clientes():
    if not os.path.exists("clientes.csv"):
        with open("clientes.csv", "w", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Codigo", "Nome", "Idade", "Telefone"])
    with open("clientes.csv", "r") as arquivo:
        linhas = arquivo.readlines()
        if linhas:
            print("\n--- Lista de Clientes ---\n")
            for linha in linhas:
                print(linha.strip())
        else:
            print("\nNenhum cliente cadastrado.")
            print("-" * 24 + "\n")
