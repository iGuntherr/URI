valor = input()
valor = valor.split(' ')
A = float(valor[0])
B = float(valor[1])
C = float(valor [2])
pi = 3.14159


triangulo = ((C * A) / 2)
circulo = (pi * ( C **2))
trapezio = (((A + B) * C) / 2)
quadrado = (B ** 2 )
retangulo = (A * B)

print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(triangulo, circulo, trapezio, quadrado, retangulo))