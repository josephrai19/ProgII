# Eliminar elemento (primera coincidencia)
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Intento de eliminar por índice
thislist.pop(2)
print("Después de pop(2):", thislist)