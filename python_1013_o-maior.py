valor = input()
valor = valor.split(' ')

a = int(valor[0])
b = int(valor[1])
c = int(valor[2])

maiorAB = ((a + b + abs( a - b)) / 2)
maiorABC = int((maiorAB + c + abs(maiorAB - c)) / 2)

print('{} eh o maior'.format(maiorABC))