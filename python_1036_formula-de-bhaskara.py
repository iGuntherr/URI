valor = input()
valor = valor.split(' ')
a = float(valor[0])
b = float(valor[1])
c = float(valor[2])
delta = ((b**2) - 4 * a * c)
bask1 = 0.00
bask2 = 0.00

if delta > 0 and a > 0:
    bask1 = (((-1) * b) + (delta**(1/2))) / (2 * a)
    bask2 = (((-1) * b) - (delta**(1/2))) / (2 * a)
    
    print('R1 = {:.5f}\nR2 = {:.5f}'.format(bask1, bask2))

else:
    print('Impossivel calcular')