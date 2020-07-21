x = int(input())
y = int(input())
a = (x if x < y else y)
b = (y if y > x else x) +1
soma = 0

for i in range(a, b):
    if (i % 13) != 0:
        soma += i 

print(soma)