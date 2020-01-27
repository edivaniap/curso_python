# Função Reduce
# Recebe uma lista e retorna um unico valor da lista

# Exemplo: obter a soma de valores de uma lista

from functools import reduce

def soma(x, y):
    return x + y

lista = [1, 3, 10, 20, 50]

sum = reduce(soma, lista)

print(lista)
print(sum)

