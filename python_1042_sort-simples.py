lista = input().split()
lista = [int(lista[0]), int(lista[1]), int(lista[2])]
lista_ord = sorted(lista)

print('{}\n{}\n{}\n\n{}\n{}\n{}'.format(lista_ord[0], lista_ord[1], lista_ord[2], lista[0], lista[1], lista[2]))
