a, b = map(int, input().split())
lista = []

for i in range(1, b + 1):
  lista.append(i)

  if(len(lista) == a):
    print(' '.join(map(str, lista)))
    lista = []