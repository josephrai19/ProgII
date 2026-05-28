# Agregar contenido al archivo (modo "a" - append)
with open("archivo_demo.txt", "a") as f:
    f.write("¡Ahora el archivo tiene más contenido!")

# Leer el archivo después de agregar contenido
with open("archivo_demo.txt") as f:
    print(f.read())

# Sobrescribir el contenido del archivo (modo "w" - write)
with open("archivo_demo.txt", "w") as f:
    f.write("¡Ups! ¡He borrado el contenido!")

# Leer el archivo después de sobrescribirlo
with open("archivo_demo.txt") as f:
    print(f.read())