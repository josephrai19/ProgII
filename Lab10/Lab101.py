with open("archivo_demo.txt", "w", encoding="utf-8") as f:
    f.write("¡Hola! Bienvenido a archivo_demo.txt\n")
    f.write("Este archivo es para fines de prueba.\n")
    f.write("¡Buena suerte!")

# Forma 1: con with (no necesita cerrar manualmente)
with open("archivo_demo.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Forma 2: abriendo y cerrando manualmente
f = open("archivo_demo.txt", encoding="utf-8")
print(f.readline())
f.close()