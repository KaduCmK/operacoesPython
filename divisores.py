# Calcular divisores de dado número

numero = int(input('Número a ser calculado: '))


def calcularDivisores(num):
    index = 0
    divisores = []
    for i in range(1, num+1):
        if num % i == 0:
            divisores.append(i)
            index += 1
    print('O Numero', num, 'tem', index, 'divisores.')
    print('Que são:', divisores)


calcularDivisores(numero)
