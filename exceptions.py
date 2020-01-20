# tratamento de exceções

a = 6
b = 0

try:
    print(a/b)
except:
    print("Não é permitido divisão por zero")

print("Ok, tudo normal, exceção foi tratada")