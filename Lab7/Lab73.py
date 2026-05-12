def contar_palabras_unicas(texto):
    palabras = texto.lower().split()
    unicas = []
    for p in palabras:
        if p not in unicas:
            unicas.append(p)
    return len(unicas)

def palabra_mas_larga(texto):
    palabras = texto.split()
    larga = ""
    for p in palabras:
        if len(p) > len(larga):
            larga = p
    return larga

def frecuencia_caracteres(texto):
    # Solo contamos letras
    total = 0
    # diccionario como en el Lab 5
    frecuencias = {}
    
    for letra in texto.lower():
        if letra.isalpha(): # Si es una letra
            total += 1
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    
    # Imprimir los porcentajes
    for l in frecuencias:
        porcentaje = (frecuencias[l] / total) * 100
        print(f"Letra {l}: {porcentaje}%")

# Parte principal
t = input("Ingrese el texto largo: ")
print("Palabras unicas:", contar_palabras_unicas(t))
print("Palabra mas larga:", palabra_mas_larga(t))
print("Frecuencia:")
frecuencia_caracteres(t)