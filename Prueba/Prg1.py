# Modificación 4.1
matriz = [
    [4, 1, 7],
    [2, 9, 3],
    [5, 8, 6]
]

suma = 0

for fila in matriz:
    for elemento in fila:
        if elemento > 5:
            suma += elemento

print(suma)


# Modificación 4.2
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