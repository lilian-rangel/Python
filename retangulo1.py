
linha = int(input("Digite a largura: "))
coluna = int(input("Digite a altura: "))

a = 0
b = 0
while a < coluna:
    while b < linha:
        print("#", end = "")
        b += 1
    print()

    a += 1
    b = 0