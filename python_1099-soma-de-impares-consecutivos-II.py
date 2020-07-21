n = int(input())

for i in range (n):
    x = input().split()
    a, b = x 
    if int(a) > int(b):
        maior = int(a)
        menor = int(b) + 1
    else:
        maior = int(b)
        menor = int(a) + 1
    impar = 0
    for i in range(menor, maior): 
        if (i%2) != 0:
            impar += i 
    print(impar)