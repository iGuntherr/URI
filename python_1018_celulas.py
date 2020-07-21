valor = int(input())
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0

print(valor)

while valor >= 100:
    n100 += 1
    valor -= 100

else:
    while valor >= 50:
        n50 += 1
        valor -= 50
    else:
        while valor >= 20:
            n20 += 1
            valor -= 20
        else:
            while valor >= 10:
                n10 += 1
                valor -= 10
            else:
                while valor >= 5:
                    n5 += 1
                    valor -= 5
                else:
                    while valor >= 2:
                        n2 += 1
                        valor -= 2
                    else:
                        while valor >=1:
                            n1 += 1
                            valor -= 1

print('{} nota(s) de R$ 100,00'.format(n100))
print('{} nota(s) de R$ 50,00'.format(n50))
print('{} nota(s) de R$ 20,00'.format(n20))
print('{} nota(s) de R$ 10,00'.format(n10))
print('{} nota(s) de R$ 5,00'.format(n5))
print('{} nota(s) de R$ 2,00'.format(n2))
print('{} nota(s) de R$ 1,00'.format(n1))