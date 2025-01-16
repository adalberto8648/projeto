# W
# Se o arquivo não existir, ele será criado.
# Se o arquivo já existir, ele será sobrescrito, apagando todos os dados existentes.

#Exemplo de uso: Gravar dados novos sem se preocupar com os existentes.
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Escrevendo dados.\n")

# a
# O arquivo deve já existir para adicionar o novo conteúdo ao final, sem apagar os dados anteriores.

#Exemplo de uso: Adicionar informações ao final do arquivo, como registros contínuos.
with open("arquivo.txt", "a") as arquivo:
    arquivo.write("Adicionando nova linha.\n")

# r
# O arquivo de já existir para exibição. Não é possível modificar o conteúdo do arquivo.
#Exemplo de uso: Ler o conteúdo de um arquivo existente.
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
