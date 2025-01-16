from tabulate import tabulate
import csv
import os
import main

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
    if not os.path.exists("fornecedores.csv"):
        with open("fornecedores.csv", "w", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Codigo", "Nome"])

    while True:
        codigo_fornecedor = input("Digite o código do fornecedor: ")
        if codigo_fornecedor.isdigit():
            break
        print("O código do fornecedor deve conter apenas números.")

    while True:
        nome_fornecedor = input("Digite o nome do fornecedor: ").strip()

        # verifica duplicidade no arquivo csv
        with open("fornecedores.csv", "r", newline="") as arquivo:
            # converte cada linha em uma lista
            conversor = csv.reader(arquivo)
            # listado, vai para uma variável
            dados = list(conversor)
        fornecedor_existe = any(fornecedor[1].strip().lower() == nome_fornecedor.lower() for fornecedor in dados[1:])
        if fornecedor_existe:
            print("Fornecedor já cadastrado. Digite outro fornecedor.")
        elif nome_fornecedor:
            break
        else:
            print("Campo em branco, digite o nome do fornecedor.")

    with open("fornecedores.csv", "a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([codigo_fornecedor, nome_fornecedor])        
    print("\nFornecedor cadastrado com sucesso")
    
def listar_fornecedores():
    # Verifica se o arquivo existe
    if not os.path.exists("fornecedores.csv"):
        print("Nenhum fornecedor cadastrado ainda.")
        # Não permiti a passagem por não existir, retorna para menu
        return

    # Lê os dados do arquivo CSV
    with open("fornecedores.csv", "r", newline="") as arquivo:
        # converte cada linha em uma lista
        conversor = csv.reader(arquivo)
        # Listado, vai para uma variável
        dados = list(conversor)

    # Verifica se há dados além do cabeçalho
    if len(dados) <= 1:
        print("Nenhum fornecedor cadastrado ainda.")
        return
    
    # Exibe os dados em formato de tabela
    print("\n--Lista de Fornecedores--\n")
    # seleciona todos os dados da lista dados, exceto o primeiro item
    # Usa o primeiro item da lista dados
    # Aplica o formato de tabela
    print(tabulate(dados[1:], headers=dados[0], tablefmt="fancy_grid"))
       
if __name__ == "__main__":
    main.acessar_projeto()