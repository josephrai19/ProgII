# Lab72.py
n = int(input("Ingrese un numero par para la matriz: "))

if n % 2 != 0:
    print("El numero no es par")
else:
    # Creamos la matriz vacía primero
    for i in range(n):
        for j in range(n):
            if i == j:
                print("1", end="\t")
            else:
                print("0", end="\t")
        print() # Esto hace el salto de línea