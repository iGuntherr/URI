dinheiro = float(input())
dinheiro += 0.001
cedulas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
print('NOTAS:')
for cedula in cedulas:
    count = dinheiro / cedula
    resto = dinheiro % cedula
    dinheiro = resto
    print('{} nota(s) de R$ {:.2f}'.format(int(count), cedula))
    
print('MOEDAS:')
for moeda in moedas:
    count = dinheiro / moeda
    resto = dinheiro % moeda
    dinheiro = resto
    print('{} moeda(s) de R$ {:.2f}'.format(int(count), moeda))