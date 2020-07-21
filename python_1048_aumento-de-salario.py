sal = float(input())
porc = (15, 12, 10, 7, 4)
reaj = sal

if sal <= 400.00:
    reaj *= (porc[0] / 100)
    sal += reaj
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %'.format(sal, reaj, porc[0]))

elif 800.00 >= sal > 400.00:
    reaj *= (porc[1] / 100)
    sal += reaj
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %'.format(sal, reaj, porc[1]))

elif 1200.00 >= sal > 800.00:
    reaj *= (porc[2] / 100)
    sal += reaj
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %'.format(sal, reaj, porc[2]))

elif 2000.00 >= sal > 1200.00:
    reaj *= (porc[3] / 100)
    sal += reaj
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %'.format(sal, reaj, porc[3]))
else:
    reaj *= (porc[4] / 100)
    sal += reaj
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %'.format(sal, reaj, porc[4]))
