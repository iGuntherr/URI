d = int(input())

a = 0
m = 0

while d >= 365:
    d -= 365
    a += 1

else:
    while d >= 30:
        d -= 30
        m += 1

print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(a, m, d))
