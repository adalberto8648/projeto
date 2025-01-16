from tabulate import tabulate
import csv
import os
import main

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

        if codigo_cliente.isdigit():
            # verifica duplicidade no arquivo csv (só exibição r)
            with open("clientes.csv", "r", newline="") as arquivo:
                # converte cada linha em uma lista
                conversor = csv.reader(arquivo)
                # listado, vai para uma variável
                dados = list(conversor)

            codigo_existe = any(codigo[0] == codigo_cliente for codigo in dados[1:])

            if codigo_existe:
                print("Código já cadastrado. Digite outro código.")
            else:
                codigo_cliente
                break
        else:
            print("O código do cliente deve conter apenas números.")

    while True:
        nome_completo = input("Digite o nome do cliente: ").strip()
        
        # verifica duplicidade no arquivo csv (só exibição r)
        with open("clientes.csv", "r", newline="") as arquivo:
            # converte cada linha em uma lista
            conversor = csv.reader(arquivo)
            # listado, vai para uma variável
            dados = list(conversor)

        cliente_existe = any(cliente[1].strip().lower() == nome_completo.lower() for cliente in dados[1:])

        if cliente_existe:
            print("Cliente já cadastrado. Digite outro nome.")
        elif nome_completo:
            break
        else:
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
        print('O telefone deve ter 11 dígitos (DDD + números). Ex.99999999999.')

    with open("clientes.csv", "a", newline="") as arquivo:
        # csv.writer: escrever dados no CSV
        escritor = csv.writer(arquivo)
        # A função writerow() grava uma linha por vez
        escritor.writerow([codigo_cliente, nome_completo, idade, telefone_formatado])
    print("\nCliente cadastrado com sucesso")

def listar_clientes():
    # Verifica se o arquivo existe
    if not os.path.exists("clientes.csv"):
        print("Nenhum cliente cadastrado ainda.")
        # Não permiti a passagem por não existir, retorna para menu
        return

    # Lê os dados do arquivo CSV (só exibição r)
    with open("clientes.csv", "r", newline="") as arquivo:
        # converte cada linha em uma lista
        conversor = csv.reader(arquivo)
        # Listado, vai para uma variável
        dados = list(conversor)

    # Verifica se há dados além do cabeçalho
    if len(dados) <= 1:
        print("Nenhum cliente cadastrado ainda.")
        return

    # Exibe os dados em formato de tabela
    print("\n--- Lista de Clientes ---\n")
    # seleciona todos os dados da lista dados, exceto o primeiro item
    # Usa o primeiro item da lista dados
    # Aplica o formato de tabela
    print(tabulate(dados[1:], headers=dados[0], tablefmt="fancy_grid"))

if __name__ == "__main__":
    main.acessar_projeto()