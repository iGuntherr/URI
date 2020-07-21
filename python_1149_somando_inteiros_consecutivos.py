x = input().split()
a = int(x[0])
n = int(x[-1])
soma = 0

for i in range(n):
    soma += (a + i)
print(soma)