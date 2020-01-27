# Filter - pega determinada lista e filtra com determinada condição

def pares(i):
    if i % 2 == 0:
        return i

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# aplica o filtro com a função pares na lista
# a funcao filter restorna um objeto do tipo filter,
# por isso usa-se a funcao lista para converte-la
lista_pares = list(filter(pares, lista))

print("Lista original: ", lista)
print("Lista com filtro de pares: ", lista_pares)
