s = int(input())

h = 0
m = 0

while s > 60:
    s -= 60
    m += 1

else:
    while m > 60:
        m -= 60
        h += 1

print('{}:{}:{}'.format(h, m, s))