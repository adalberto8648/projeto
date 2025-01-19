import clientes
import fornecedores
import produtos

def acessar_projeto():

    print("\n------------------------ ------")
    print("|           PROJETO           |")
    print("-------------------------- ----\n")

    nome = "senha"
    senha = "123"
    
    while True:
        acesso_nome = input("Digite o nome: ")
        if acesso_nome == nome:
            break
        print("Nome inválido, digite novamente.")

    while True:
        acesso_senha = input("Digite a senha: ")
        if acesso_senha == senha:
            print("Acesso permitido.")
            break
        print("Senha inválida, digite novamente.")

    while True:
        print("\n----- Menu PROJETO -----")
        print("1 - Clientes")
        print("2 - Fornecedor")
        print("3 - Produtos")
        escolha = input("\nEscolha uma das opções: ")
        print("-" * 24 + "\n")
        
        if escolha == "1":
            clientes.menu_clientes()
        elif escolha == "2":
            fornecedores.menu_fornecedores()
        elif escolha == "3":
            produtos.menu_produtos()
        else:
            print("Opção inválida, tente novamente\n")

if __name__ == "__main__":
    acessar_projeto()