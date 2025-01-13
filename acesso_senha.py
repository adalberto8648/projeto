from cadastro_clientes import menu_cadastro

print("\n---- Acesso ao projeto ---\n")

nome = "adalberto"
senha = 123

while True:
    acesso_nome = input("Digite o nome: ").lower()
    if acesso_nome == nome:
        while True:
            try:
                acesso_senha = int(input("Digite a senha: "))
                if acesso_senha == senha:
                    break
                else:
                    print("Senha inválida, digite novamente.")
            except ValueError:
                print("Senha inválida, digite novamente.")
        break
    else:
        print("Nome inválido, digite novamente.")
        continue
    
menu_cadastro()