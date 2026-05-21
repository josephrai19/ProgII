matriz = [
    [4, 1, 7],
    [2, 9, 3],
    [5, 8, 6]
]

contador = 0

for fila in matriz:
    for elemento in fila:
        if elemento > 5:
            contador += 1

print(contador)