def soma_elementos(lista):
    soma_dos_elementos = 0
    for valores in lista:
        soma_dos_elementos += valores
    return soma_dos_elementos


lista = [1, 3, 5, 10, 25]

l = soma_elementos(lista)
print(l)