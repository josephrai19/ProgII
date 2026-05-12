n = int(input("Ingrese un numero: "))

if n < 0:
    print("No existe factorial de negativos")
else:
    f = 1
    for i in range(1, n + 1):
        f = f * i
    
    print("El factorial es:")
    print(f)