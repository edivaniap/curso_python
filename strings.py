nome = "Edivânia"
sobrenome = "Oliveira"

print("Nome: " + nome + " " + sobrenome)
print("Sigla: " + nome[0] + sobrenome[0])
print("Apelido: " + nome[0:3])
print("Etc: " + nome[:5])
print("Etc: " + nome[5:])

aux = nome + " " + sobrenome

print(aux.lower())
print(aux.upper())

# strip remove espaços (e alguns char especiais)
#no começo e fim da string
aux = "     " + nome + " " + sobrenome + "         "
print("Teste strip em: " + aux)
print("Resultado:\n" + aux.strip())


# split converte uma string em lista

minha_string = "O rato roeu a roupa do rei de Roma"
minha_lista = minha_string.split()

print(minha_lista)

minha_lista = minha_string.split("r")
print(minha_lista)

#find retorna a posicao de onde ele encontrou a chave
busca = minha_string.find("rei")
print(busca)
busca = minha_string.find("rainha")
print(busca)

# replace
minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)

