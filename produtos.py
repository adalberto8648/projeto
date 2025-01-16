from tabulate import tabulate
import csv
import os
import main

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
        if not codigo_produto or " " in codigo_produto:
            print("O código não pode ficar vazio ou ter espaços.")
        else:
            break

    while True:
        nome_produto = input("Digite o nome do produto: ").strip()
        if nome_produto:
            break
        print("Campo em branco, digite o nome do produto.")
        
    with open("produtos.csv", "a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([codigo_produto, nome_produto])        
    print("\nProduto cadastrado com sucesso")

def listar_produtos():
    # Verifica se o arquivo existe
    if not os.path.exists("produtos.csv"):
        print("Nenhum fornecedor cadastrado ainda.")
        # Não permiti a passagem por não existir, retorna para menu
        return
    
    # Lê os dados do arquivo CSV
    with open("produtos.csv", "w", newline="") as arquivo:
        # converte cada linha em uma lista
        conversor = csv.reader(arquivo)
        # Listado, vai para uma variável
        dados = list(conversor)

    # Verifica se há dados além do cabeçalho
    if len(dados) <= 1:
        print("Nenhum fornecedor cadastrado ainda.")
        return
    
    # Exibe os dados em formato de tabela
    print("\n----- Lista de produtos -----")
    # seleciona todos os dados da lista dados, exceto o primeiro item
    # Usa o primeiro item da lista dados
    # Aplica o formato de tabela
    print(tabulate(dados[1:], headers=dados[0], tablefmt="fancy_grid"))

if __name__ == "__main__":
    main.acessar_projeto()