# Calcular o MMC de dois numeros

a = int(input('Valor a: '))
b = int(input('Valor b: '))

if a > b:
    maior = a
else:
    maior = b
while True:
    if maior % a == 0 and maior % b == 0:
        print(maior)
        break
    else:
        maior += 1