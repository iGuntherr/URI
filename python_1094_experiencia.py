n = int(input())
cobaias, coelhos, ratos, sapos = 0, 0, 0, 0

for i in range(n):
    x = input().split()
    a, b = x 
    a = int(a)
    cobaias += a 
    if b == 'C':
        coelhos += a
    if b == 'R':
        ratos += a
    if b == 'S':
        sapos += a

print(
'''Total: {} cobaias
Total de coelhos: {}
Total de ratos: {}
Total de sapos: {}
Percentual de coelhos: {:.2f} %
Percentual de ratos: {:.2f} %
Percentual de sapos: {:.2f} %'''.format(cobaias, coelhos, ratos, sapos, 
                                        ((coelhos / cobaias) * 100), 
                                        ((ratos / cobaias) * 100), 
                                        ((sapos / cobaias) * 100)))