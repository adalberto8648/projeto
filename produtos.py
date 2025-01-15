import csv
import os

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
    if not os.path.exists("produtos.csv"):
        with open("produtos.csv", "w", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Codigo", "Produto"])
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
    with open("produtos.csv", "a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([codigo_produto, nome_produto])        
    print("\nProduto cadastrado com sucesso")

def listar_produtos():
    if not os.path.exists("produtos.csv"):
        with open("produtos.csv", "w", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Codigo", "Produto"])
    with open("produtos.csv", "r") as arquivo:
        linhas = arquivo.readlines()
        if linhas:
            print("\n----- Lista de produtos -----")
            for linha in linhas:
                print(linha.strip())
        else:
            print("\nNenhum Produto encontrado.")
            print("-" * 24 + "\n")
            