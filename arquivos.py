# a variavel 'arquivo' vai ser um Objeto de arquivo
arquivo = open("arquivo.txt")

print(arquivo)

# linhas vai ser uma lista com cada linha do arquivo
linhas = arquivo.readlines()

print(linhas)

##for linha in linhas:
##    print(linha)


texto_completo = arquivo.read()

print(texto_completo)

# criar arquivo limpo
arq_novo = open("arquivo2.txt", "w")
arq_novo.write("esse eh meu arquivo")

arq_novo.close()
arquivo.close()

# criar arquivo e se já existe ele concatena a escrita
arq_novo2 = open("arquivo3.txt", "a")
arq_novo2.write("esse eh meu arquivo\n")

arq_novo2.close()