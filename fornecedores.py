import csv
import os

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
        if not os.path.exists("fornecedores.csv"):
            with open("fornecedores.csv", "w", newline="") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow(["Codigo", "Nome"])
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
    with open("fornecedores.csv", "a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([codigo_fornecedor, nome_fornecedor])        
    print("\nFornecedor cadastrado com sucesso")
    
def listar_fornecedores():
    if not os.path.exists("fornecedores.csv"):
        with open("fornecedores.csv", "w", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Codigo", "Nome"])
    with open("fornecedores.csv", "r") as arquivo:
        linhas = arquivo.readlines()
        if linhas:
            print("\n--Lista de Fornecedores--\n")
            for linha in linhas:
                print(linha.strip())
        else:
            print("\nNenhum Fornecedor encontrado.")
            print("-" * 24 + "\n")
