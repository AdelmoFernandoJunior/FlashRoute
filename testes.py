def calcular_total(valor, juros):
    total = valor + (valor * juros)
    return total

resultado = calcular_total(1000, 0.10)

print(resultado)