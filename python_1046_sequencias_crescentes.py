while True:
    x = int(input())
    lista = []
    if x == 0:
        break 
    else:        
        for i in range(1, x + 1):
            lista.append(i)    
        if (len(lista) == x):
            print(' '.join(map(str, lista)))