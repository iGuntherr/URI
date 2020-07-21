n = int(input())

for i in range(1, n + 1):
    for p in range(2):
        print('{} {} {}'.format(i, (i**2) + p, (i**3) + p))