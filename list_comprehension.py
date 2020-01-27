# List Comprehension

# exemplo sem list comp.
x = [1, 2, 3, 4, 5]
y = []

for i in x:
    y.append(i ** 2)

print("X: ", x)
print("Y: ", y)

# exemplo com lis comp.

# lista = [valor laço condição]
z = [i ** 2 for i in x]
print("Z: ", z)

# outro exemplo com condição
w =[i for i in x if i % 2 == 1]
print("W: ", w)