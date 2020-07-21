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