while True:
    a, b = map(int, input().split())

    if a == b:
        break

    v = 'Crescente' if a < b else 'Decrescente'

    print(v)