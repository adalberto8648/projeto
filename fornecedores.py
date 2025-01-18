from tabulate import tabulate
import csv
import os
import main

def menu_fornecedores():
    while True:
        print("\n--- Menu Fornecedores ---")
        print("1 - Cadastrar Fornecedors")
        print("2 - Listar Fornecedores")
        print("3 - Alterar Fornecedores")
        print("4 - Menu LuPINK")
        escolha = input("\nEscolha uma opção: ")
        print("-" * 24 + "\n")

        if escolha == "1":
            cadastrar_fornecedores()
        elif escolha == "2":
            listar_fornecedores()
        elif escolha == "3":
            alterar_fornecedores()
        elif escolha == "4":
            print("Acessando -> Menu LuPINK ...")
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
            with open("fornecedores.csv", "r", newline="") as arquivo:
                conversor = csv.reader(arquivo)
                dados = list(conversor)

            codigo_existe = any(codigo[0] == codigo_fornecedor for codigo in dados[1:])
            
            if codigo_existe:
                print("Código já cadastrado. Digite outro código.")
            else:
                codigo_fornecedor
                break
        else:
            print("O código do fornecedor deve conter apenas números.")

    while True:
        nome_fornecedor = input("Digite o nome do fornecedor: ").strip()

        with open("fornecedores.csv", "r", newline="") as arquivo:
            conversor = csv.reader(arquivo)
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
    if not os.path.exists("fornecedores.csv"):
        print("Nenhum fornecedor cadastrado ainda.")
        return

    with open("fornecedores.csv", "r", newline="") as arquivo:
        conversor = csv.reader(arquivo)
        dados = list(conversor)

    if len(dados) <= 1:
        print("Nenhum fornecedor cadastrado ainda.")
        return
    
    print("\n--Lista de Fornecedores--\n")
    print(tabulate(dados[1:], headers=dados[0], tablefmt="fancy_grid"))
       
def alterar_fornecedores():
    if not os.path.exists("fornecedores.csv"):
        print("Nenhum fornecedor cadastrado ainda.")
        return
    
    while True:
        codigo_digitado = input("Digite o código do fornecedor que deseja alterar: ")

        if codigo_digitado.isdigit():
            with open("fornecedores.csv", "r", newline="") as arquivo:
                escritor = csv.reader(arquivo)
                dados = list(escritor)
            if len(dados) <= 1:
                print("Nenhum fornecedor cadastrado ainda.")
                return
            
            print(tabulate(dados[1:], headers=dados[0], tablefmt="fancy_grid" ))

            nome = None
            for linha, coluna in enumerate(dados[1:], start=1):
                if coluna[0] == codigo_digitado:
                    nome = linha
                    break
            if nome is None:
                print("Código não encontrado.")
                return
            
            novo_nome = input("Digite o novo nome para o fornecedor: ").strip()
            if not novo_nome:
                print("Nenhum nome foi informado. Voltando ao menu principal.")
                return

            dados[nome][1] = novo_nome

            with open("fornecedores.csv", "w", newline="") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerows(dados)
            print("Nome alterado com sucesso.")
            break
        else:
            print("O código do fornecedor deve conter apenas números.")
    
if __name__ == "__main__":
    main.acessar_projeto()