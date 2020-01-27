# Função Zip
# Compacta duas listas como se fossem uma unica
# Da para imprimir duas listas simultaneamente
lista1 = [1, 2, 3, 4, 5]
lista2 = ["rihanna", "beyonce", "lana del rey", "lizzo", "doja cat"]


for numero, nome in zip(lista1, lista2):
    print(numero, nome)

# exemplo com 3 listas

lista3 = ["love on the brain", "formation", "lust for life", "truth hurts", "rules"]

for num, artista, musica in zip(lista1, lista2, lista3):
    print(num, ":", artista, "-", musica)