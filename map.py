# Map

def dobro(x):
    return x * 2

valores = [1, 2, 3, 4, 5]

# com a funcao map podemos passar cada valor por 
# uma funcao aplicando o resultado de seu retorno.
# ela retorna um objeto do tipo map e precisamos converte-la em lista

print(list(map(dobro, valores)))