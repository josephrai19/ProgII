matriz = [
    [4, 1, 7],
    [2, 9, 3],
    [5, 8, 6]
]

suma = 0

for fila in matriz:
    for elemento in fila:
        if elemento % 2 == 0:
            suma += elemento

print(suma)

# 1. que hace este programa? ¿que imprime?
# El programa recorre una matriz de número que a su vez realiza 
# una suma siempre y cuando sea par de los números pares e imprime el resultado de dicha suma.

# 2. explica como recorren la matriz los ciclos.
# El primer ciclo recorre cada fila de la matriz.
# El segundo ciclo recorre cada número dentro de cada fila.

# 3. que condición se evalua dentro del if
# Evaluar si el número es par mediante una división o residuo

# 5. Por elementos: se trabajan directo con los valores de la matriz
#    Por índices: se trabaja usando posiciones de filas y columnas