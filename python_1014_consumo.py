X = int(input())
Y = float(input())
Y = float('{:1}'.format(Y))

CONSUMO = ( X / Y)

print('{:.3f} km/l'.format(CONSUMO))