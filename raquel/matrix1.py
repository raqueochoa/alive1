matrix = [
[],
[],
[]
]

n = 1
x = 0
sum = 0
y = 0

for x in matrix:
    for y in range(0,3):
        x.append(int(input(f'Ingresa primer valor de la lista {n}: ')))
    n += 1
