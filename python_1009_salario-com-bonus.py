nome = input()
salario = float(input())
comissao = float(input())

comissao *= 0.15
TOTAL = float(salario + comissao)

print('TOTAL = R$ {:.2f}'.format(TOTAL))