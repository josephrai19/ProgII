# Ejemplo de 3 funciones de validación de cadena en Python

clave = "Admin123"
puntuacion = "500"
espacios = "   "

# isalnum()
print("¿Es 'Admin123' alfanumérico?:", clave.isalnum())

# isdigit()
print("¿Es '500' un dígito?:", puntuacion.isdigit())

# isspace()
print("¿La variable contiene solo espacios?:", espacios.isspace())