while True:
    x = input().split()
    a, b = x
    a = int(a)
    b = int(b)

    if a > b: 
        maior = a
        menor = b
    else:
        maior = b
        menor = a 
    
    if menor <= 0:
        break
    s = ''
    sm = 0
    for i in range(menor, (maior + 1)):
        if i == menor:
            s += str(i)
        else: 
            s += " "
            s += str(i)
        sm += i
    print('{} Sum={}'.format(s, sm))