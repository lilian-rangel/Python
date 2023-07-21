def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista = [1, 1, 2, 3, 4, 4, 6, 5, 10, 8, 7, 5]

lista = remove_repetidos(lista)
print(lista)
