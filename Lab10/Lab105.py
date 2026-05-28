class Factorial:
    def calcular(self, n):
        if n < 0:
            return "No existe factorial de números negativos"
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

n = int(input("Ingresa un número para calcular su factorial: "))
f = Factorial()
print(f"El factorial de {n} es: {f.calcular(n)}")