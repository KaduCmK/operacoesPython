# calcular o MDC de 2 números:

a = int(input('Numero 1: '))
b = int(input('Numero 2: '))

def calcular_mdc(a, b):
    if a < b:
        divisor = a
    else:
        divisor = b
    while True:
        if a % divisor == 0 and b % divisor == 0:
            print('MDC =', divisor)
            break
        else:
            divisor -= 1

calcular_mdc(a, b)