NUMBER = int(input())
horas = int(input())
valor_hora = float(input())

valor_hora = float('{0:2}'.format(valor_hora))

SALARY = float(horas * valor_hora)

print('NUMBER = {}\nSALARY = U$ {:.2f}'.format(NUMBER, SALARY))