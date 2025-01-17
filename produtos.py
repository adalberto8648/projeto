from tabulate import tabulate
import csv
import os
import main

def menu_produtos():
    while True:
        print("\n---- Menu Produtos ----")
        print("1 - Cadastrar Produtos")
        print("2 - Listar Produtos")
        print("3 - Menu LuPINK")
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            cadastrar_produtos()
        elif escolha == "2":
            listar_produtos()
        elif escolha == "3":
            print("Acessando -> Menu LuPINK ...")
            break
        else:
            print("\nCódigo inválido, digite novamente")

def cadastrar_produtos():
    if not os.path.exists("produtos.csv"):
        with open("produtos.csv", "w", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Codigo", "Produto"])

    while True:
        codigo_produto = input("Digite o código do produto: ")

        if codigo_produto.isdigit():
            with open("produtos.csv", "r", newline="") as arquivo:
                conversor = csv.reader(arquivo)
                dados = list(conversor)

            codigo_existe = any(codigo[0] == codigo_produto for codigo in dados[1:])
            
            if codigo_existe:
                print("Código já cadastrado. Digite outro código.")
            else:
                codigo_produto
                break
        else:
            print("O código do produto deve conter apenas números.")

    while True:
        nome_produto = input("Digite o nome do produto: ").strip()

        if nome_produto:
            break
        else:
            print("Campo em branco, digite o nome do produto.")
        
    with open("produtos.csv", "a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([codigo_produto, nome_produto])        
    print("\nProduto cadastrado com sucesso")

def listar_produtos():
    if not os.path.exists("produtos.csv"):
        print("Nenhum produto cadastrado ainda.")
        return
    
    with open("produtos.csv", "r", newline="") as arquivo:
        conversor = csv.reader(arquivo)
        dados = list(conversor)

    if len(dados) <= 1:
        print("Nenhum produto cadastrado ainda.")
        return
    
    print("\n----- Lista de produtos -----")
    print(tabulate(dados[1:], headers=dados[0], tablefmt="fancy_grid"))

if __name__ == "__main__":
    main.acessar_projeto()