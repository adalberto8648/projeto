import clientes
import fornecedores
import produtos

print("\n---- Acesso ao projeto ----\n")

def acessar_projeto():
    nome = "adalberto"
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
        print("\n----- Menu Projeto -----")
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

acessar_projeto()

# proximos passos
# validar se os dados já estão presentes no CSV antes de cadastrar um novo item, para evitar duplicações.
# adicionar uma opção para editar um registro existente no CSV, permitindo alterar informações como nome, idade, telefone, etc.
# Quando listar os dados, exibir os dados em formato de tabela, para ficar mais legível.