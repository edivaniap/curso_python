print("while:")

i = 0

while i < 5:
    print(i)
    i += 1 

print("--------")

i = 0

while i <= 10:
    print(i)
    i += 2 

print("--------")

print("for:")

for i in range(6,10):
    print(i)

print("--------")

print("for:")

for i in range(0,5):
    print(i)

print("--------")

lista1 = [1, 2, 3, 4, 5]
lista2 = ["ola", "mundo", "!"]
lista3 = [0, "ola", "rihanna", 9.99, True]

print(">> lista 1")
for i in lista1:
    print(i)

print(">> lista 2")
for i in lista2:
    print(i)
    
print(">> lista 3")
for i in lista3:
    print(i)