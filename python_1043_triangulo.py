a, b, c = map(float, input().split())

lados = None
area = None
perimetro = None

if ((b - c) < a < (b + c)) and ((a - c) < b < (a + c)) and ((a - b) < c < (a + b)):
    lados = 3
else:
    lados = 4

if lados == 3:
    perimetro = a + b + c
    print('Perimetro = {:.1f}'.format(perimetro))
else:
    area = ((a + b) * c) / 2
    print('Area = {:.1f}'.format(area))