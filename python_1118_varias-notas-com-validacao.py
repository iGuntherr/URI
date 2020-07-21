msg = 1

while msg == 1:
    n, m = 0, 0
    while True:
        x = float(input())

        if 0 <= x <= 10:
            n += x 
            m += 1
        else:
            print('nota invalida')
        
        if m >= 2:
            break

    print('media = {:.2f}'.format((n/m)))

    while True:
        print('novo calculo (1-sim 2-nao)')
        msg = int(input())
        if 1 <= msg <= 2:
            break 
