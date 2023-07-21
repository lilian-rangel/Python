linha = int(input("Digite a largura: "))
coluna = int(input("Digite a altura: "))

a = 0
b = 0
while a < coluna:
    b = 0
    while b < linha:
        if a == 0 or a == coluna-1 or b == 0 or b == linha-1:
            print("#" , end = "")
        else:
            print(" " , end = "")
        b += 1
    print()
    a += 1