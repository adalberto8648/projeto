from tabulate import tabulate
import csv
import os
import main
import clientes

def menu_produtos():
    while True:
        print("\n---- Menu Produtos ----")
        print("1 - Cadastrar Produtos")
        print("2 - Listar Produtos")
        print("3 - Alterar Produtos")
        print("4 - Menu PROJETO")
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            cadastrar_produtos()
        elif escolha == "2":
            listar_produtos()
        elif escolha == "3":
            alterar_produtos()
        elif escolha == "4":
            print("Acessando -> Menu PROJETO ...")
            break
        else:
            print("\nCódigo inválido, digite novamente")

def cadastrar_produtos():
    if not os.path.exists("produtos.csv"):
        with open("produtos.csv", "w", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Codigo", "Produto"])

    dados = clientes.abrir_arquivo_r("produtos.csv")
    
    while True:
        codigo_produto = input("Digite o código do produto: ")
        if codigo_produto.isdigit():

            codigo_existe = any(codigo[0] == codigo_produto for codigo in dados[1:])
            
            if codigo_existe:
                print("Código já cadastrado. Digite outro código.")
            else:
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
    
    dados = clientes.abrir_arquivo_r("produtos.csv")
    
    print("\n----- Lista de produtos -----\n")
    print(tabulate(dados[1:], headers=dados[0], tablefmt="fancy_grid"))

def alterar_produtos():
    if not os.path.exists("produtos.csv"):
        print("Nenhum produto cadastrado ainda.")
        return
    
    dados = clientes.abrir_arquivo_r("produtos.csv")

    while True:
        codigo_digitado = input("Digite o código do produto que deseja alterar: ")

        if codigo_digitado.isdigit():
            
            print(tabulate(dados[1:], headers=dados[0], tablefmt="fancy_grid"))

            linha_encontrada = None
            for linha, coluna in enumerate(dados[1:], start=1):
                if coluna[0] == codigo_digitado:
                    linha_encontrada = linha
                    break
            
            if linha_encontrada is None:
                print("Código não encontrado.")
                return
            
            novo_nome = input("Digite o novo nome para o produto: ").strip()

            dados[linha_encontrada][1] = novo_nome

            with open("produtos.csv", "w", newline="") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerows(dados)

            print("Nome alterado com sucesso.")
            break
        else:
            print("O código do produto deve conter apenas números.")

if __name__ == "__main__":
    main.acessar_projeto()