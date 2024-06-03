def maior_num(a, b):
    if a > b:
        return a
    else:
        return b

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

maior_numero = maior_num(numero1, numero2)
print("O maior número é:", maior_numero)