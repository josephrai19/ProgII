# Leer línea por línea con readline()
with open("archivo_demo.txt") as f:
    print(f.readline())
    print(f.readline())

# Recorrer todo el archivo con un for
with open("archivo_demo.txt") as f:
    for x in f:
        print(x)