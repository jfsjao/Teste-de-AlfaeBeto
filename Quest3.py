def soma_lista(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma

lista = [1, 2, 55, 4, 5]
print("O resultado da lista: ")
resultado = soma_lista(lista)
print(resultado)  # imprime 15