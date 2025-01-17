from tabulate import tabulate
import csv
import os
import main

def menu_clientes():
    while True:
        print("\n----- Menu clientes -----")
        print("1 - Cadastrar Clientes")
        print("2 - Listar Clientes")
        print("3 - Menu LuPINK")
        escolha = input("\nEscolha uma opção: ")
        print("-" * 24 + "\n")
        
        if escolha == "1":
            cadastrar_clientes()
        elif escolha == "2":
            listar_clientes()
        elif escolha == "3":
            print("Acessando -> Menu LuPINK ...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

def cadastrar_clientes():
    if not os.path.exists("clientes.csv"):

        # r - só exibição
        # w - criação o usubistituição do arquivo csv
        # a - adiciona dados
        # newline = Elimina a duplicidade de linha em branco no final
        with open("clientes.csv", "w", newline="") as arquivo:
            # writer - escrever dados no CSV
            escritor = csv.writer(arquivo)
            # csv.writerow() grava uma linha, método do objeto csv.writer()
            escritor.writerow(["Codigo", "Nome", "Idade", "Telefone"])

    while True:
        codigo_cliente = input("Digite o código do cliente: ")

        if codigo_cliente.isdigit():
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
        
        with open("clientes.csv", "r", newline="") as arquivo:
            conversor = csv.reader(arquivo)
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
        escritor = csv.writer(arquivo)
        escritor.writerow([codigo_cliente, nome_completo, idade, telefone_formatado])
    print("\nCliente cadastrado com sucesso")

def listar_clientes():
    if not os.path.exists("clientes.csv"):
        print("Nenhum cliente cadastrado ainda.")
        # retorna para menu
        return

    with open("clientes.csv", "r", newline="") as arquivo:
        conversor = csv.reader(arquivo)
        dados = list(conversor)
    # len - conta quantas linhas inclusive cabeçalho
    if len(dados) <= 1:
        print("Nenhum cliente cadastrado ainda.")
        return

    # Exibe os dados em formato de tabela
    print("\n--- Lista de Clientes ---\n")

    # dados[1:] - seleciona todos os dados da lista dados, começando da segunda linha
    # headers=dados[0] - define o cabeçalho
    # tablefmt= - formatação da tabela
    print(tabulate(dados[1:], headers=dados[0], tablefmt="fancy_grid"))

if __name__ == "__main__":
    main.acessar_projeto()