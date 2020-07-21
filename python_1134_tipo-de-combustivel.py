a, g, d = 0, 0, 0

while True:
    msg = int(input())

    if msg == 1:
        a += 1
    elif msg == 2:
        g += 1
    elif msg == 3:
        d += 1
    elif msg == 4:
        break

print('''MUITO OBRIGADO
Alcool: {}
Gasolina: {}
Diesel: {}'''.format(a, g, d))