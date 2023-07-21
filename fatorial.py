fatorial = int(input("Digite o valor de n: "))
resultado = 1
contador = 1
while contador <= fatorial:
    resultado *= contador
    contador += 1
print(resultado)