import random

# random.seed(1) - força o python a selecionar sempre o mesmo número

# gera numero de 0 ate 10
aleatorio = random.randint(0,10)
print(aleatorio)

# choice() - seleciona um item de uma lista
lista = [45, 23, 65, 54, 35]
aleatorio = random.choice(lista)
print(aleatorio)