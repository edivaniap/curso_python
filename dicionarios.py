# declaraçao
meu_dicionario = { "A":"Ameixa", "B":"Bola", "C":"Cachorro"}
print(meu_dicionario["A"])
print(meu_dicionario["B"])
print(meu_dicionario["C"])
print(meu_dicionario)

print("-----")

for chave in meu_dicionario:
    print("chave: ", chave, " / valor: ", meu_dicionario[chave])

for i in meu_dicionario.items():
    print(i)

for v in meu_dicionario.values():
    print(v)

for k in meu_dicionario.keys():
    print(k)