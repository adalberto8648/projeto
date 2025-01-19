from tabulate import tabulate
import csv
import os
import main

def menu_clientes():
    while True:
        print("\n----- Menu clientes -----")
        print("1 - Cadastrar Clientes")
        print("2 - Listar Clientes")
        print("3 - Alterar Clientes")
        print("4 - Menu PROJETO")
        escolha = input("\nEscolha uma opção: ")
        print("-" * 24 + "\n")
        
        if escolha == "1":
            cadastrar_clientes()
        elif escolha == "2":
            listar_clientes()
        elif escolha == "3":
            alterar_cliente()
        elif escolha == "4":
            print("Acessando -> Menu PROJETO ...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

def cadastrar_clientes():

    # se não existe o arquivo, vai criar
    if not os.path.exists("clientes.csv"):

        # with open com w - vai criar o arquivo
        # r - só exibição
        # w - criação o usubistituição do arquivo csv
        # a - adiciona dados
        # newline = elimina a duplicidade de linha em branco no final
        with open("clientes.csv", "w", newline="") as arquivo:
            # writer - escrever dados no CSV
            escritor = csv.writer(arquivo)
            # csv.writerow() grava uma linha, método do objeto csv.writer()
            escritor.writerow(["Codigo", "Nome", "Idade", "Telefone"])

    while True:
        codigo_cliente = input("Digite o código do cliente: ")

        # se codigo_cliente tem só número
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

    print("\n--- Lista de Clientes ---\n")

    # dados[1:] - seleciona todos os dados da lista dados, começando da segunda linha
    # headers=dados[0] - define o cabeçalho
    # tablefmt= - formatação da tabela
    print(tabulate(dados[1:], headers=dados[0], tablefmt="fancy_grid"))

def abrir_arquivo_r(nome_arquivo):
    with open(nome_arquivo, "r", newline="") as arquivo:
        escritor = csv.reader(arquivo)
        dados = list(escritor)
    if len(dados) <= 1:
        print("Nenhum cadastro encontrado.")
        return None
    print(tabulate(dados[1:], headers=dados[0], tablefmt="fancy_grid"))
    return dados

def alterar_cliente():
    if not os.path.exists("clientes.csv"):
        print("Nenhum cliente cadastrado ainda.")
        return

    while True:
        codigo_digitado = input("Digite o código do cliente que deseja alterar: ")

        if codigo_digitado.isdigit():
            
            dados = abrir_arquivo_r("cliente.csv")
            if dados is None:
                print("Nenhum cliente cadastrado ainda.")
                return
            

            # None - definido que não foi encontrado nome, tipo uma lista_vazia mas não é uma lista
            nome = None
            # for - pra cada linha, na coluna não definida ainda
            # enumerate - gera índice pegando os dados da 2º linha, enumerando começando de 1
            for linha, coluna in enumerate(dados[1:], start=1):
                # se (definindo coluna 0) que é a primeira, estiver o código
                if coluna[0] == codigo_digitado:
                    # manda pra variável a linha encontrada e segue
                    nome = linha
                    break
                
            if nome is None:
                print("Código não encontrado.")
                return
            
            novo_nome = input("Digite o novo nome para o cliente: ").strip()
            if not novo_nome:
                print("Nenhum nome foi informado. Voltando ao menu principal.")
                return
            
            nova_idade = input("Digite a nova idade para o cliente: ")
            if not nova_idade.isdigit():
                print("Nenhuma idade foi informado. Voltando ao menu principal.")
                return
            
            novo_telefone = input("Digite o novo telefone para o cliente: ")
            if not len(novo_telefone) == 11 and novo_telefone.isdigit():
                print('O telefone deve ter 11 dígitos (DDD + números). Ex.99999999999.')
                return
            novo_telefone_formatado = f"({novo_telefone[:2]}) {novo_telefone[2:7]}-{novo_telefone[7:]}"
            
            # atualiza o dado na matriz
            # dados[nome] - foi determinado anteriormente quando encontramos o nome na linha
            # [1] - refere-se à 2° coluna e pega o novo nome e coloca no lugar
            dados[nome][1] = novo_nome
            dados[nome][2] = nova_idade
            dados[nome][3] = novo_telefone_formatado

            # reescreve o arquivo com os dados atualizados
            with open("clientes.csv", "w", newline="") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerows(dados)
            print("Dados do cliente alterados com sucesso.")
            break
        else:
            print("O código do cliente deve conter apenas números.")            

if __name__ == "__main__":
    main.acessar_projeto()

    