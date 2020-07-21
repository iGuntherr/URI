x = int(input())
y = int(input())
a = (x if x < y else y) + 1
b = (y if y > x else x) 

for i in range(a, b):
    if 2 == (i%5) or 3 == (i%5):
        print(i)