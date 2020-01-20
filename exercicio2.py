# Média

nota1 = float(input("Digite  a primeira nota: "))
nota2 = float(input("Digite  a segunda nota: "))

media = (nota1 + nota2) / 2

print("Sua média é: ", media)

if media >= 6:
    print("Status: Aprovado")
elif media >= 0:
    print("Status: Reprovado")
else:
    print("Média inválida")