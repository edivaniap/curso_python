minha_lista_1 = ["game of thrones", "rick and morty", "blindspot"] 
minha_lista_2 = [1, 2, 3, 4, 5]
minha_lista_3 = ["cafe", 2, 9.89, True]

print(minha_lista_1)
print(minha_lista_2)
print(minha_lista_3)

print(minha_lista_1[1])

print("----")

for item in minha_lista_1:
    print(item)

print("Tamanho lista 1: ", len(minha_lista_1))

# adicionar elementos na lista
minha_lista_1.append("orphan black")

print(minha_lista_1) 

# verificando se elemento existe numa lista
if 7 in minha_lista_2:
    print("7 esta na lista 2")
else:
    print("7 não está na lista 2")

if 3 in minha_lista_2:
    print("3 esta na lista 2")
else:
    print("3 não está na lista 2")

# remover elementos na lista
del minha_lista_1[2]
print(minha_lista_1)
# del minha_lista_1[2:] - remove do indice 2 ao final
# del minha_lista_1[:2] - remove do indice inicial 0 ate o item 2
# del minha_lista_1[:] - remove do todos itens
# del minha_lista_1 - remove toda lista, inclusive a variavel 

del minha_lista_1[:]
print(minha_lista_1)

# ------------- ORDENACAO
lista = [455, 56, 5, 478, 212, 1, 0, 6, 25]
print(lista)

# sorted() retorna lista ordenada
lista2 = sorted(lista)
print(lista2)

# sort() ordena e aplica na propria lista 
lista.sort()
print(lista)

# ordenar de maneira decrescente 
lista.sort(reverse=True)
print(lista)

# apenas inverter a lista
lista = [455, 56, 5, 478, 212, 1, 0, 6, 25]
lista.reverse()
print(lista)

print("----------------")
lista3 = ["bola", "alicate", "dinheiro", "carro"]
print(lista3)
lista3.sort()
print(lista3)